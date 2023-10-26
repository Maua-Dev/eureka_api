from app.controllers.user.get_all_users_controller import GetAllUsersController
from app.environments import Environments
from app.helpers.http.django_http_request import DjangoHttpRequest
from app.helpers.http.django_http_response import DjangoHttpResponse


repo = Environments.get_user_repo()()

class UserViews:
    @staticmethod
    def get_all_users(request):
        controller = GetAllUsersController(repo)
        http_request = DjangoHttpRequest(request)
        response = controller(http_request)
        http_response = DjangoHttpResponse(body=response.body, status_code=response.status_code,
                                           message=response.message)
        return http_response.to_django()