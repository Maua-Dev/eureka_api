from django.http import JsonResponse


class DjangoHttpResponse:
    status_code: int = 200
    body: dict = {}
    message: str = "Valid request"
    
    def __init__(self, body: dict = {}, status_code: int = 200, message: str = "Valid request"):
        self.status_code = status_code
        self.body = body
        
    def to_django(self, **kwargs):
        return JsonResponse(
            {
                "body": self.body, 
                "message": self.message
            }, 
            safe= kwargs.get("safe", False), 
            status=self.status_code
        )
            