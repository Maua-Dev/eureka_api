from app.controllers.professor.get_all_professors_controller import GetAllProfessorsController
from app.helpers.http.django_http_request import DjangoHttpRequest
from app.helpers.http.django_http_response import DjangoHttpResponse
from app.models.repos.professor.professor_repo_mock import ProfessorRepoMock

repo = ProfessorRepoMock()

class ProfessorViews:
    @staticmethod
    def get_all_professors(request):
        print(f"\n\n==== {repo.get_all_professors()} ====\n\n")
        controller = GetAllProfessorsController(repo)
        http_request = DjangoHttpRequest(request)
        response = controller(http_request)
        http_response = DjangoHttpResponse(body=response.body, status_code=response.status_code, message=response.message)

        return http_response.to_django()
