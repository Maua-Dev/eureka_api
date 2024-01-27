from app.controllers.controller_interface import IController
from app.helpers.errors.common_errors import MissingParameters, WrongTypeParameter
from app.helpers.http.http_codes import InternalServerError, BadRequest, OK
from app.helpers.http.http_models import HttpRequestModel
from app.repos.project.project_repository_interface import IProjectRepository


class GetProjectsByRoleController(IController):

    def __init__(self, repo: IProjectRepository):
        super().__init__(repo)
        self.repo = repo

    def __call__(self, request: HttpRequestModel):
        try:
            self.error_handling(request)
            response_data = self.business_logic(request)

            return OK(
                body=response_data,
                message="The project were retrieved successfully"
            )

        except MissingParameters as err:
            return BadRequest(message=err.message)
        
        except WrongTypeParameter as err:
            return BadRequest(
                message=err.message
            )

        except Exception as err:
            return InternalServerError(
                message=str(err)
            )

    def error_handling(self, request: HttpRequestModel):
        if request.method != "GET":
            raise MissingParameters('body', 'get_projects_by_role')

        data = request.data
        if data.get('user_id') is None:
            raise MissingParameters('user_id', 'get_projects_by_role')

        if type(request.data.get('user_id')) == str:
            if not request.data.get('user_id').isdecimal():
                raise WrongTypeParameter('user_id')
            else:
                request.data['user_id'] = int(request.data['user_id'])

        elif type(request.data.get('user_id')) != int:
            raise WrongTypeParameter('user_id')


    def business_logic(self, request: HttpRequestModel):
        return self.repo.get_projects_by_role(request.data)
