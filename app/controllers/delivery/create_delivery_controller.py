import json

from app.controllers.controller_interface import IController
from app.helpers.errors.common_errors import MissingParameters
from app.helpers.http.http_codes import Created, BadRequest, InternalServerError
from app.helpers.http.http_models import HttpRequestModel
from app.repos.delivery.delivery_repository_interface import IDeliveryRepository
from app.repos.project.project_repository_interface import IProjectRepository
from app.repos.task.task_repository_interface import ITaskRepository


class CreateDeliveryController(IController):

    def __init__(self, delivery_repo: IDeliveryRepository, task_repo: ITaskRepository, project_repo: IProjectRepository): 
        super().__init__(delivery_repo=delivery_repo, task_repo=task_repo, project_repo=project_repo)
        self.delivery_repo = delivery_repo
        self.task_repo = task_repo
        self.project_repo = project_repo

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

        except Exception as e:
            return InternalServerError(
                message=str(e)
            )

    def error_handling(self, request: HttpRequestModel):
        if request.method != "POST":
            raise MissingParameters('body', 'create_delivery')

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
        
        
        
        response = self.delivery_repo.create_delivery(delivery)

        return response
