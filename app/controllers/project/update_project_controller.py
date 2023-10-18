from app.controllers.controller_interface import IController
from app.helpers.errors.common_errors import MissingParameters
from app.helpers.http.http_codes import InternalServerError, BadRequest, OK
from app.helpers.http.http_models import HttpRequestModel
from app.repos.project.project_repository_interface import IProjectRepository


class UpdateProjectController(IController):
    def __init__(self, repo: IProjectRepository):
        super().__init__(repo)
        self.repo = repo

    def __call__(self, request: HttpRequestModel):
        try:
            self.error_handling(request)
            response_data = self.business_logic(request)

            return OK(
                body=response_data,
                message="The project was updated successfully"
            )

        except MissingParameters as err:
            return BadRequest(message=err.message)

        except Exception as err:
            return InternalServerError(
                message=str(err)
            )

    def error_handling(self, request: HttpRequestModel):
        if request.method != "PUT":
            raise MissingParameters('body', 'update_project')

        data = request.data

        if data.get('project_id') is None:
            raise MissingParameters('project_id', 'update_project')

    def business_logic(self, request: HttpRequestModel):
        return self.repo.update_project(request.data)
