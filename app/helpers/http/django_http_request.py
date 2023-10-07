import json
from app.helpers.http.http_models import HttpRequestModel

class DjangoHttpRequest(HttpRequestModel):
    data: dict = {}
    method: str
    
    def __init__(self, request, **kwargs):
        super().__init__(request, **kwargs)