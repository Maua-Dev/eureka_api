from django.test import TestCase

from app.controllers.delivery.get_deliveries_controller import GetDeliveriesController
from app.helpers.http.django_http_request import DjangoHttpRequest
from app.repos.delivery.delivery_repository_mock import DeliveryRepositoryMock


class Test_GetDeliveriesController(TestCase):

    def test_get_deliveries_controller(self):
        repo = DeliveryRepositoryMock()
        controller = GetDeliveriesController(repo)
        request = DjangoHttpRequest(
            request=None,
            data={
                "project_id": 1,
            },
            method="GET"
        )
        response = controller(request)

        assert response.status_code == 200
        assert type(response.body) == list
