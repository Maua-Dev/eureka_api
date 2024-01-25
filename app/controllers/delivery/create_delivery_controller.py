import json

from app.controllers.controller_interface import IController
from app.helpers.errors.common_errors import MissingParameters
from app.helpers.http.http_codes import Created, BadRequest, InternalServerError
from app.helpers.http.http_models import HttpRequestModel
from app.repos.delivery.delivery_repository_interface import IDeliveryRepository


class CreateDeliveryController(IController):

    def __init__(self, repo: IDeliveryRepository): 
        super().__init__(repo)
        self.repo = repo

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
        """
        try:
            project_set = Project.objects.get(project_id=delivery['project_id'])
            user_set = User.objects.get(user_id=delivery['user_id'])
            task_set = Task.objects.get(task_id=delivery['task_id'])
        except:
            return None

        if not project_set or not user_set or not task_set:
            return None

        user = user_set.to_dict()
        project = project_set.to_dict()
        task = task_set.to_dict()

        if task['responsible'] == 'ADVISOR' and user['role'] != 'ADVISOR':
            return None
        if task['responsible'] == 'RESPONSIBLE' and user['role'] != 'RESPONSIBLE':
            return None

        students_id = [student['user_id'] for student in project['students']]
        if user['role'] == 'STUDENT' and user['user_id'] not in students_id:
            return None

        professors_id = [professor['user_id'] for professor in project['professors']]
        if user['role'] == 'PROFESSOR' and user['user_id'] not in professors_id:
            return None

        delivery = Delivery.objects.create(
            task=task_set,
            project=project_set,
            user=user_set,
            content=delivery['content']
        )
        delivery.save()

        delivery_dict = delivery.to_dict()

        return delivery_dict
        """
        response = self.repo.create_delivery(request.data)

        return response
