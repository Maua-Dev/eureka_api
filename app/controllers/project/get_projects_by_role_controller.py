from app.controllers.controller_interface import IController
from app.helpers.errors.common_errors import MissingParameters, UserNotFound, WrongTypeParameter
from app.helpers.http.http_codes import InternalServerError, BadRequest, OK, NotFound
from app.helpers.http.http_models import HttpRequestModel
from app.repos.project.project_repository_interface import IProjectRepository
from app.repos.user.user_repository_interface import IUserRepository


class GetProjectsByRoleController(IController):

    def __init__(self, project_repo: IProjectRepository, user_repo: IUserRepository):
        super().__init__(project_repo)
        self.project_repo = project_repo
        self.user_repo = user_repo

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

        except UserNotFound as err:
            return NotFound(
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

        user_id = request.data["user_id"]

        user = self.user_repo.get_user(user_id)

        if user is None:
            raise UserNotFound()

        return self.project_repo.get_projects_by_role(user_id=user_id)
