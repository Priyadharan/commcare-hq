from dimagi.utils.couch.database import get_db
from django.http import HttpResponse
import json
from restkit.errors import RequestFailed

DEFAULT_DISPLAY_LENGTH = "10"
DEFAULT_START = "0"
DEFAULT_ECHO = "0"


class DatatablesParams(object):
    
    def __init__(self, count, start, desc, echo):
        self.count = count
        self.start = start
        self.desc = desc
        self.echo = echo
        
    @classmethod
    def from_request_dict(cls, query):
        
        count = int(query.get("iDisplayLength", DEFAULT_DISPLAY_LENGTH));
        
        start = int(query.get("iDisplayStart", DEFAULT_START));
        
        # sorting
        desc_str = query.get("sSortDir_0", "desc")
        desc = desc_str == "desc"
        
        echo = query.get("sEcho", DEFAULT_ECHO)
        return DatatablesParams(count, start, desc, echo)
        
        

class CouchPaginator(object):
    """
    Allows pagination of couchdbkit ViewResult objects.
    This class is meant to be used in conjunction with datatables.net
    ajax APIs, to allow you to paginate your views efficiently.
    """
    
    
    def __init__(self, view_name, generator_func, search=True, search_preprocessor=lambda x: x, use_reduce_to_count=0, view_args={}):
        """
        The generator function should be able to convert a couch 
        view results row into the appropriate json.
        
        No searching will be done unless you pass in a search view
        """
        self._view = view_name
        self._generator_func = generator_func
        self._search = search
        self._search_preprocessor = search_preprocessor
        self._view_args = view_args
        
    def get_ajax_response(self, request, default_display_length=DEFAULT_DISPLAY_LENGTH, 
                          default_start=DEFAULT_START, extras={}):
        """
        From a datatables generated ajax request, return the appropriate
        httpresponse containing the appropriate objects objects.
        
        Extras allows you to override any individual paramater that gets 
        returned
        """
        query = request.REQUEST
        params = DatatablesParams.from_request_dict(query)
        
        # search
        search_key = query.get("sSearch", "")
        if self._search and search_key:
            items = get_db().view(self._view, skip=params.start, limit=params.count, descending=params.desc, key=self._search_preprocessor(search_key), reduce=False, **self._view_args)
            if params.start + len(items) < params.count:
                total_display_rows = len(items)
            else:
                total_display_rows = get_db().view(self._view, key=self._search_preprocessor(search_key), reduce=True).one()["value"]
            total_rows = items.total_rows
                
        else:
            # only reduce if the _search param is set.  
            # TODO: get this more smartly from the couch view
            kwargs = {}
            if self._search:
                kwargs.update(skip=params.start, limit=params.count, descending=params.desc, reduce=False)
                kwargs.update(self._view_args)
            else:
                kwargs.update(skip=params.start, limit=params.count, descending=params.desc)
                kwargs.update(self._view_args)
            items = get_db().view(self._view, **kwargs)
            total_rows = items.total_rows
            total_display_rows = items.total_rows

        
        # this startkey, endkey business is not currently used, 
        # but is a better way to search eventually.
        # for now the skip parameter is fast enough to suit our scale
        startkey, endkey = None, None
        all_json = []
        for row in items:
            if not startkey:
                startkey = row["key"]
            endkey = row["key"]
            row = self._generator_func(row)
            if row:
                all_json.append(row)
        
        to_return = {"sEcho": params.echo,
                     "iTotalDisplayRecords": total_display_rows,
                     "iTotalRecords": total_rows,
                     "aaData": all_json}
        
        for key, val in extras.items():
            to_return[key] = val
        
        return HttpResponse(json.dumps(to_return))


class LucenePaginator(object):
    """
    Allows pagination of couchdbkit ViewResult objects, integrated with 
    lucene.  This is a slightly different model than the other one, though
    the functionality could probably be shared better.
    """
    
    
    def __init__(self, search_view_name, generator_func): 
        """
        The generator function should be able to convert a couch 
        view results row into the appropriate json.
        """
        self._search_view = search_view_name
        self._generator_func = generator_func
        
    def get_ajax_response(self, request, search_query, extras={}):
        """
        From a datatables generated ajax request, return the appropriate
        httpresponse containing the appropriate objects objects.
        
        Extras allows you to override any individual paramater that gets 
        returned
        """
        query = request.POST if request.method == "POST" else request.GET
        params = DatatablesParams.from_request_dict(query)
        
        results = get_db().search(self._search_view, q=search_query,
                                  handler="_fti/_design", 
                                  limit=params.count, skip=params.start)
        all_json = []
        try:
            for row in results:
                row = self._generator_func(row)
                if row is not None:
                    all_json.append(row)
            total_rows = results.total_rows
        except RequestFailed, e:
            # just ignore poorly formatted search terms for now
            total_rows = 0
            
        
        to_return = {"sEcho": params.echo,
                     "iTotalDisplayRecords": total_rows,
                     "aaData": all_json}
        
        for key, val in extras.items():
            to_return[key] = val
        
        return HttpResponse(json.dumps(to_return))


class ReportBase(object):
    extras = {}
    def __init__(self, request):
        self.request = request
    @classmethod
    def ajax_view(cls, *args, **kwargs):
        return cls(*args, **kwargs).get_ajax_response()
    def get_ajax_response(self):
        """
        From a datatables generated ajax request, return the appropriate
        httpresponse containing the appropriate objects objects.

        Extras allows you to override any individual paramater that gets
        returned
        """
        params = DatatablesParams.from_request_dict(self.request.REQUEST)

        count = self.count()
        to_return = {
            "sEcho": params.echo,
            "iTotalDisplayRecords": count,
            "iTotalRecords": count,
            "aaData": self.rows(params.start, params.count)
        }

        to_return.update(self.extras)

        return HttpResponse(json.dumps(to_return))
    def count(self):
        raise NotImplemented()
    def rows(self, skip, limit):
        raise NotImplemented()