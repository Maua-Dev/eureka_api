import json

from app.controllers.controller_interface import IController
from app.helpers.errors.common_errors import MissingParameters
from app.helpers.http.http_codes import Created
from app.helpers.http.http_models import HttpRequestModel
from app.repos.delivery.delivery_repository_interface import IDeliveryRepository


class CreateDeliveryController(IController):

    def __init__(self, repo: IDeliveryRepository):
        super().__init__(repo)
        self.repo = repo

    def __call__(self, request: HttpRequestModel):
        self.error_handling(request)
        response_data = self.business_logic(request)

        return Created(
            body=response_data,
            message="The delivery was created successfully"
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
        if type(request.data['content']) == str:
            request.data['content'] = request.data['content'].encode('utf-8')

        if type(request.data['content']) == dict:
            request.data['content'] = json.dumps(request.data['content']).encode('utf-8')

        response = self.repo.create_delivery(request.data)

        content_decode = response['content'].decode('utf-8') if type(response['content']) == bytes else None

        response['content'] = content_decode if content_decode is not None else response['content']

        response['content'] = eval(response['content']) if type(response['content']) != str else response['content']

        return response
