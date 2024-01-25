import json

from app.controllers.controller_interface import IController
from app.helpers.errors.common_errors import AdvisorForbiddenAction, ObjectNotFound, MissingParameters, ProjectNotFound, RequestNotFound, RoleForbiddenAction, StudentForbiddenAction, TaskNotFound, UserNotFound
from app.helpers.http.http_codes import Created, BadRequest, InternalServerError, NotFound, Forbidden
from app.helpers.http.http_models import HttpRequestModel
from app.repos.delivery.delivery_repository_interface import IDeliveryRepository
from app.repos.project.project_repository_interface import IProjectRepository
from app.repos.task.task_repository_interface import ITaskRepository
from app.repos.user.user_repository_interface import IUserRepository


class CreateDeliveryController(IController):

    def __init__(self, delivery_repo: IDeliveryRepository, task_repo: ITaskRepository, project_repo: IProjectRepository, user_repo: IUserRepository): 
        super().__init__(delivery_repo=delivery_repo, task_repo=task_repo, project_repo=project_repo, user_repo=user_repo)

    def __call__(self, request: HttpRequestModel):

        try:
            self.error_handling(request)
            response_data = self.business_logic(request)

            return Created(
                body=response_data,
                message="The delivery was created successfully"
            )

        except MissingParameters as e:
            return BadRequest(
                message=str(e)
            )

        except ObjectNotFound as e:
            return NotFound(
                message=str(e)
            )

        except RoleForbiddenAction as e:
            return Forbidden(
                message=str(e)
            )

        except Exception as e:
            return InternalServerError(
                message=str(e)
            )

    def error_handling(self, request: HttpRequestModel):
        try:
            if request.method != "POST":
                raise Exception()
        except:
            raise RequestNotFound()
        
        
        if request.data.get('task_id') is None:
            raise MissingParameters('task_id', 'create_delivery')

        if request.data.get('project_id') is None:
            raise MissingParameters('project_id', 'create_delivery')

        if request.data.get('user_id') is None:
            raise MissingParameters('user_id', 'create_delivery')

        if request.data.get('content') is None:
            raise MissingParameters('content', 'create_delivery')


    def business_logic(self, request: HttpRequestModel):
        delivery = request.data
        
        try:
            task = self.task_repo.get_task(delivery['task_id'])
            if task is None:
                raise Exception()
        except:
            raise TaskNotFound()
        try:
            project = self.project_repo.get_project(delivery['project_id'])
            if project is None:
                raise Exception()
        except:
            raise ProjectNotFound()
        try:
            user = self.user_repo.get_user(delivery['user_id'])
            if user is None:
                raise Exception()
        except:
            raise UserNotFound()
        
        if task['responsible'] == 'ADVISOR' and user['role'] not in ['RESPONSIBLE', "ADVISOR"]:
            raise StudentForbiddenAction()
        if task['responsible'] == 'RESPONSIBLE' and user['role'] != 'RESPONSIBLE':
            if user['role'] == 'ADVISOR':
                raise AdvisorForbiddenAction()
            raise StudentForbiddenAction()
        
        # students_id = [student['user_id'] for student in project['students']]
        # if user['role'] == 'STUDENT' and user['user_id'] not in students_id:
        #     return None
        # professors_id = [professor['user_id'] for professor in project['professors']]
        # if user['role'] == 'PROFESSOR' and user['user_id'] not in professors_id:
        #     return None
        
        response = self.delivery_repo.create_delivery(
            delivery=delivery, 
            user=user, 
            task=task, 
            project=project
        )

        return response
