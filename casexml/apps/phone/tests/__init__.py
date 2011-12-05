from dimagi.utils.logging import log_exception
try:
    from .test_ota_restore import *
    from .test_sync_token_updates import *
    from .test_case_purging import *
except ImportError, e:
    # for some reason the test harness squashes these so log them here for clarity
    # otherwise debugging is a pain
    log_exception(e)
    raise(e)
