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
                "content": {"content": "Algum conteúdo"},
                "delivery_date": "2023-09-20"
            }

        len_before = len(repo.deliveries)
        repo.create_delivery(delivery)

        assert len(repo.deliveries) == len_before + 1

    def test_get_delivery(self):
        repo = DeliveryRepositoryMock()
        delivery = repo.get_delivery(1)
        assert delivery == repo.deliveries[0]

    def test_get_deliveries(self):
        repo = DeliveryRepositoryMock()
        deliveries = repo.get_deliveries(1)
        assert deliveries == repo.deliveries

