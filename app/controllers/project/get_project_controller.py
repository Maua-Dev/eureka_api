from app.controllers.controller_interface import IController
from app.helpers.errors.common_errors import MissingParameters, ProjectNotFound
from app.helpers.http.http_codes import InternalServerError, BadRequest, OK, NotFound
from app.helpers.http.http_models import HttpRequestModel
from app.repos.project.project_repository_interface import IProjectRepository


class GetProjectController(IController):
    def __init__(self, repo: IProjectRepository):
        super().__init__(repo)
        self.repo = repo

    def __call__(self, request: HttpRequestModel): 
        try:
            self.error_handling(request)
            response_data = self.business_logic(request)

            if response_data is None:
                raise ProjectNotFound()

            return OK(
                body=response_data,
                message="The project was retrieved"
            )

        except MissingParameters as err:
            return BadRequest(message=err.message)

        except ProjectNotFound as err:
            return NotFound(
                message=err.message
            )

        except Exception as err:
            return InternalServerError(
                message=str(err)
            )

    def error_handling(self, request: HttpRequestModel):
        if request.method != "GET":
            raise MissingParameters('method', 'get_project')

        data = request.data

        if data.get('project_id') is None:
            raise MissingParameters('project_id', 'get_project')

    def business_logic(self, request: HttpRequestModel):
        return self.repo.get_project(request.data['project_id'])
