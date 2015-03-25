from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.encoding import smart_str
import pytz
import datetime
import dateutil
from corehq.apps.domain.models import Domain
from corehq.apps.users.models import CouchUser, WebUser
from dimagi.utils.logging import notify_exception


def coerce_timezone_value(value):
    try:
        return pytz.timezone(str(value))
    except pytz.UnknownTimeZoneError:
        raise ValidationError("Unknown timezone")


def validate_timezone_max_length(max_length, zones):
    def reducer(x, y):
        return x and (len(y) <= max_length)
    if not reduce(reducer, zones, True):
        raise Exception("corehq.apps.timezones.fields.TimeZoneField MAX_TIMEZONE_LENGTH is too small")


def string_to_pretty_time(date_string, to_tz, from_tz=pytz.utc, fmt="%b %d, %Y %H:%M"):
    try:
        date = datetime.datetime.replace(dateutil.parser.parse(date_string), tzinfo=from_tz)
        date = _adjust_datetime_to_timezone(date, from_tz.zone, to_tz.zone)
        return date.strftime(fmt)
    except Exception:
        return date_string


def is_timezone_in_dst(tz, compare_time=None):
    now = datetime.datetime.now(tz=tz) if not compare_time else tz.localize(compare_time)
    transitions = []
    if not hasattr(tz, '_utc_transition_times'):
        return False

    # todo: should be cleaned up to not rely on the internals of pytz
    for dst_transition in tz._utc_transition_times:
        if dst_transition.year == now.year:
            transitions.append(tz.localize(dst_transition))
    if len(transitions) >= 2 and (transitions[0] <= now <= transitions[1]):
        return True
    return False


def get_timezone_for_user(couch_user_or_id, domain):
    # todo cleanup
    timezone = None
    if couch_user_or_id:
        if isinstance(couch_user_or_id, CouchUser):
            requesting_user = couch_user_or_id
        else:
            assert isinstance(couch_user_or_id, basestring)
            try:
                requesting_user = WebUser.get_by_user_id(couch_user_or_id)
            except CouchUser.AccountTypeError:
                return pytz.utc
        domain_membership = requesting_user.get_domain_membership(domain)
        if domain_membership:
            timezone = coerce_timezone_value(domain_membership.timezone)

    if not timezone:
        current_domain = Domain.get_by_name(domain)
        try:
            timezone = coerce_timezone_value(current_domain.default_timezone)
        except pytz.UnknownTimeZoneError:
            timezone = pytz.utc
    return timezone
