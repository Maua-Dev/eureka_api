from app.controllers.controller_interface import ControllerInterface
from app.helpers.http.django_http_request import DjangoHttpRequest
from app.helpers.http.http_codes import OK, InternalServerError
from app.repos.professor.professor_repo_interface import ProfessorRepoInterface


class GetAllProfessorsController(ControllerInterface):
    def __init__(self, repo: ProfessorRepoInterface):
        self.repo = repo
    
    def __call__(self, request: DjangoHttpRequest):
        try:
            self.error_handling(request)
            response_data = self.business_logic(request)
            
            return OK(
                body=response_data,
                message="The professors were successfully retrieved"
            )
            
        except Exception as err:
            return InternalServerError(
                message=str(err)
            )
    
    def error_handling(self, request: DjangoHttpRequest):
        pass
    
    def business_logic(self, request: DjangoHttpRequest):
        return self.repo.get_all_professors()
