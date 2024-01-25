from django.test import TestCase

from app.controllers.delivery.create_delivery_controller import CreateDeliveryController
from app.helpers.http.django_http_request import DjangoHttpRequest
from app.repos.delivery.delivery_repository_mock import DeliveryRepositoryMock
from app.repos.delivery.delivery_repository_postgres import DeliveryRepositoryPostgres
from app.repos.project.project_repository_mock import ProjectRepositoryMock
from app.repos.project.project_repository_postgres import ProjectRepositoryPostgres
from app.repos.task.task_repository_mock import TaskRepositoryMock
from app.repos.task.task_repository_postgres import TaskRepositoryPostgres


class Test_CreateDeliveryController(TestCase):

    def test_create_delivery_controller(self):
        delivery_repo = DeliveryRepositoryPostgres()
        project_repo = ProjectRepositoryPostgres()
        task_repo = TaskRepositoryPostgres()
        controller = CreateDeliveryController(delivery_repo=delivery_repo, project_repo=project_repo, task_repo=task_repo)
        request = DjangoHttpRequest(
            request=None,
            data={
                "task_id": 1,
                "project_id": 1,
                "user_id": 3,
                "content": {
                    "key": "value"
                }
            },
            method="POST"
        )
        response = controller(request)

        assert response.status_code == 201
