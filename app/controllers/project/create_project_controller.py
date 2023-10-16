from app.controllers.controller_interface import IController
from app.helpers.errors.common_errors import MissingParameters
from app.helpers.http.http_codes import Created, InternalServerError, BadRequest
from app.helpers.http.http_models import HttpRequestModel
from app.repos.project.project_repository_interface import IProjectRepository


class CreateProjectController(IController):

    def __init__(self, repo: IProjectRepository):
        super().__init__(repo)
        self.repo = repo

    def __call__(self, request: HttpRequestModel):
        try:
            self.error_handling(request)
            response_data = self.business_logic(request)

            return Created(
                body=response_data,
                message="The project was created successfully"
            )

        except MissingParameters as err:
            return BadRequest(message=err.message)

        except Exception as err:
            return InternalServerError(
                message=str(err)
            )

    def error_handling(self, request: HttpRequestModel):
        if request.method != "POST":
            raise MissingParameters('body', 'create_project')

        data = request.data
        if data.get('title') == None:
            raise MissingParameters('title', 'create_project')

        if data.get('qualification') is None:
            raise MissingParameters('qualification', 'create_project')

        if data.get('code') is None:
            raise MissingParameters('code', 'create_project')

        if data.get('shift') is None:
            raise MissingParameters('shift', 'create_project')

        if data.get('stand_number') is None:
            raise MissingParameters('stand_number', 'create_project')

        if data.get('is_entrepreneurship') is None:
            raise MissingParameters('is_entrepreneurship', 'create_project')

        if data.get('professors') is None:
            raise MissingParameters('professors', 'create_project')

    def business_logic(self, request: HttpRequestModel):
        return self.repo.create_project(request.data)
