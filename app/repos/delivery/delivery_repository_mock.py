from typing import Dict, List

from app.repos.delivery.delivery_repository_interface import IDeliveryRepository


class DeliveryRepositoryMock(IDeliveryRepository):
    deliveries: List[Dict[str, str]]

    def __init__(self):
        self.deliveries = [
            {
                "delivery_id": 1,
                "task": 1,
                "project": 1,
                "user": 4,
                "content": "Algum conteúdo",
                "delivery_date": "2023-05-15"
            },
            {
                "delivery_id": 2,
                "task": 2,
                "project": 1,
                "user": 1,
                "content": "Orientador do projeto",
                "delivery_date": "2023-05-22"
            },
            {
                "delivery_id": 3,
                "task": 3,
                "project": 1,
                "user": 2,
                "content": "Responsável pelo projeto",
                "delivery_date": "2023-09-14"
            },
            {
                "delivery_id": 4,
                "task": 4,
                "project": 1,
                "user": 5,
                "content": "Algum conteúdo Aluno de novo",
                "delivery_date": "2023-10-01"
            },
            {
                "delivery_id": 5,
                "task": 5,
                "project": 1,
                "user": 3,
                "content": "Aprovado",
                "delivery_date": "2023-10-03"
            },
            {
                "delivery_id": 6,
                "task": 6,
                "project": 1,
                "user": 5,
                "content": "Algum conteúdo",
                "delivery_date": "2023-09-17"
            },
            ]


    def create_delivery(self, delivery):
        delivery["delivery_id"] = len(self.deliveries) + 1
        self.deliveries.append(delivery)
