from app.controllers.controller_interface import IController
from app.helpers.errors.common_errors import MissingParameters
from app.helpers.http.http_codes import InternalServerError, OK, BadRequest
from app.helpers.http.http_models import HttpRequestModel
from app.repos.project.project_repository_interface import IProjectRepository


class CreateController(IController):

    def __init__(self, repo: IProjectRepository):
        super().__init__(repo)
        self.repo = repo

    def __call__(self, request: HttpRequestModel):
        try:
            self.error_handling(request)
            response_data = self.business_logic(request)

            return OK(
                body=[project.to_dict() for project in response_data] if type(response_data[0]) != dict else response_data, # TODO: Refactor this (entity? repo use to dict? idk)
                message="All tasks were successfully retrieved"
            )

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(
                message=str(err)
            )

    def error_handling(self, request: HttpRequestModel):
        if request.POST is None:
            raise MissingParameters('body', 'create_project')

        data = request.POST
        if data.get('title') is None:
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
        return self.repo.create_project(request.POST)
