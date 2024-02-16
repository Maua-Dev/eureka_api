from app.controllers.controller_interface import IController
from app.helpers.errors.common_errors import UserAlreadyInProject, MissingParameters, WrongTypeParameter, UserNotFound
from app.helpers.http.http_codes import Created, Forbidden, InternalServerError, BadRequest, NotFound
from app.helpers.http.http_models import HttpRequestModel
from app.repos.project.project_repository_interface import IProjectRepository
from app.repos.user.user_repository_interface import IUserRepository


class CreateProjectController(IController):

    def __init__(self, project_repo: IProjectRepository, user_repo: IUserRepository):
        super().__init__(project_repo)
        self.project_repo = project_repo
        self.user_repo = user_repo

    def __call__(self, request: HttpRequestModel):
        try:
            self.error_handling(request)
            response_data = self.business_logic(request)

            return Created(
                body=response_data,
                message="The project was created successfully"
            )
        except UserNotFound as err:
            return NotFound(message=err.message)
            
        except WrongTypeParameter as err:
            return BadRequest(message=err.message)

        except UserAlreadyInProject as err:
            return Forbidden(message=err.message)

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

        if data.get('students') is not None:
            if not isinstance(data['students'], list):
                raise WrongTypeParameter('students')
            
        if data.get('advisors') is not None:
            if not isinstance(data['advisors'], list):
                raise WrongTypeParameter('advisors')
            
        if data.get('responsibles') is not None:
            if not isinstance(data['responsibles'], list):
                raise WrongTypeParameter('responsibles')

    def business_logic(self, request: HttpRequestModel):
        if request.data.get('students') is not None:
            for student_id in request.data['students']:
                student = self.user_repo.get_user(user_id=student_id)
                if student is None:
                    raise UserNotFound()
                
                student_projects = self.repo.get_projects_by_role(user_id=student_id)
                if student_projects != []:
                    raise UserAlreadyInProject(role="Estudante")
                
        if request.data.get('advisors') is not None:
            for advisor_id in request.data['advisors']:
                advisor = self.user_repo.get_user(user_id=advisor_id)
                if advisor is None:
                    raise UserNotFound()
                
        if request.data.get('responsible') is not None:
            for responsible_id in request.data['responsible']:
                responsible = self.user_repo.get_user(user_id=responsible_id)
                if responsible is None:
                    raise UserNotFound()
        
        return self.repo.create_project(request.data)
