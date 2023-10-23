from django.test import TestCase

from app.repos.delivery.delivery_repository_mock import DeliveryRepositoryMock


class Test_DeliveryRepositoryMock(TestCase):
    def test_create_delivery(self):
        repo = DeliveryRepositoryMock()
        delivery = {
                "delivery_id": 7,
                "task": 7,
                "project": 1,
                "user": 3,
                "content": "Algum conteúdo",
                "delivery_date": "2023-09-20"
            }

        len_before = len(repo.deliveries)
        repo.create_delivery(delivery)

        assert len(repo.deliveries) == len_before + 1

