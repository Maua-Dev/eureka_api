from app.controllers.professor.get_all_professors_controller import GetAllProfessorsController
from app.environments import Environments
from app.helpers.http.django_http_request import DjangoHttpRequest
from app.helpers.http.django_http_response import DjangoHttpResponse

repo = Environments.get_professor_repo()()

class ProfessorViews:
    @staticmethod
    def get_all_professors(request):
        controller = GetAllProfessorsController(repo)
        http_request = DjangoHttpRequest(request)
        response = controller(http_request)
        http_response = DjangoHttpResponse(body=response.body, status_code=response.status_code, message=response.message)

        return http_response.to_django()
