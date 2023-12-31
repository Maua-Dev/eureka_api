from app.controllers.project.create_project_controller import CreateProjectController
from app.controllers.project.get_project_controller import GetProjectController
from app.controllers.project.update_project_controller import UpdateProjectController
from app.environments import Environments
from app.helpers.http.django_http_request import DjangoHttpRequest
from app.helpers.http.django_http_response import DjangoHttpResponse

repo = Environments.get_project_repo()()


class ProjectViews:
    @staticmethod
    def create_project(request):
        controller = CreateProjectController(repo)
        http_request = DjangoHttpRequest(request)
        response = controller(http_request)
        http_response = DjangoHttpResponse(body=response.body, status_code=response.status_code,
                                           message=response.message)

        return http_response.to_django()

    @staticmethod
    def update_project(request):
        controller = UpdateProjectController(repo)
        http_request = DjangoHttpRequest(request)
        response = controller(http_request)
        http_response = DjangoHttpResponse(body=response.body, status_code=response.status_code,
                                           message=response.message)

        return http_response.to_django()

    @staticmethod
    def get_project(request):
        controller = GetProjectController(repo)
        http_request = DjangoHttpRequest(request)
        response = controller(http_request)
        http_response = DjangoHttpResponse(body=response.body, status_code=response.status_code,
                                           message=response.message)

        return http_response.to_django()
