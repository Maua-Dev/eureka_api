from django.test import TestCase

from app.controllers.delivery.create_delivery_controller import CreateDeliveryController
from app.helpers.http.django_http_request import DjangoHttpRequest
from app.repos.delivery.delivery_repository_mock import DeliveryRepositoryMock


class Test_CreateDeliveryController(TestCase):

    def test_create_delivery_controller(self):
        repo = DeliveryRepositoryMock()
        controller = CreateDeliveryController(repo)
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
