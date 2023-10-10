from django.http import JsonResponse

from app.helpers.http.http_models import HttpResponseModel

class DjangoHttpResponse(HttpResponseModel):
    status_code: int = 200
    body: dict = {}
    message: str = "Valid request"
    
    def __init__(self, body: dict = {}, status_code: int = 200, message: str = "Valid request"):
       super().__init__(body=body, status_code=status_code, message=message)
        
    def to_django(self, **kwargs):
        return JsonResponse(
            {
                "body": self.body, 
                "message": self.message
            }, 
            safe= kwargs.get("safe", False), 
            status=self.status_code
        )
            