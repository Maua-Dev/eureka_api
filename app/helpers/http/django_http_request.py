import json
from django.core.handlers.wsgi import WSGIRequest

from app.helpers.errors.common_errors import MissingParameters
from app.helpers.errors.http_errors import ConflictInParameters
class DjangoHttpRequest:
    data: dict = {}
    method: str
    
    def __init__(self, request, **kwargs):
        
        if type(request) == WSGIRequest:
            if request.body == None:
                raise MissingParameters('body', 'DjangoHttpRequest.__init__')
            if request.method == None:
                raise MissingParameters('method', 'DjangoHttpRequest.__init__')
            
            self.data = json.loads(request.body.decode('utf-8'))            
            self.method = request.method
        
        if type() == dict:
            if len(kwargs) != 0:
                intersections = set(self.data.keys()).intersection(kwargs.keys())
                if len(intersections):
                    raise ConflictInParameters(str(intersections), "self.data", "kwargs", "DjangoHttpRequest.__init__")
                self.data.update(kwargs)