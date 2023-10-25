import json
from django.core.handlers.wsgi import WSGIRequest

class HttpRequestModel:
    data: dict
    method: str
    
    def __init__(self, request, **kwargs):
        self.data = {}
        if type(request) == WSGIRequest:
            if(len(request.body) == 0):
                data = {}
            else:
                print(request.body.decode('utf-8'))
                self.data = json.loads(request.body.decode('utf-8'))

            self.method = request.method
            if self.method == "GET":
                self.data.update(request.GET.dict())

        if type(kwargs) == dict:
            data = kwargs.get("data")
            if(data != None):
                self.data.update(data)
            
            method = kwargs.get("method")
            if(method != None):
                self.method = method

    def __repr__(self):
        return (
            f"HttpRequest (data={self.data}, method={self.method})"
        )


class HttpResponseModel:
    status_code: int = 200
    body: dict
    message: str = "Valid request"
    
    def __init__(self, body: dict, status_code: int = 200, message: str = "Valid request"):
        self.status_code = status_code
        self.body = body
        self.message = message

    def __repr__(self):
        return (
            f"HttpResponse (status_code={self.status_code}, body={self.body}, message={self.message})"
        )

