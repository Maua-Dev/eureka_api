from django.test import TestCase

from app.repos.delivery.delivery_repository_mock import DeliveryRepositoryMock


class Test_DeliveryRepositoryMock(TestCase):
    def test_create_delivery(self):
        repo = DeliveryRepositoryMock()
        delivery = {
            "delivery_id": 7,
            "task_id": 7,
            "project_id": 1,
            "user_id": 3,
            "content": {"content": "Algum conteúdo"},
            "delivery_date": "2023-09-20"
        }
        project = {
            'project_id': 1,
            'title': 'Teste',
            'qualification': 'Engenharia da Computação',
            'code': 'ECOM000',
            'shift': 'DIURNO',
            'stand_number': '1',
            'is_entrepreneurship': False,
            'professors': [
                {
                    'user_id': 4,
                    'name': 'CARLOS EDUARDO DANTAS DE MENEZES',
                    'email': 'carlos.menezes@maua.br',
                    'role': 'ADVISOR'
                },
                {
                    'user_id': 5,
                    'name': 'ANA PAULA GONCALVES SERRA',
                    'email': 'ana.serra@maua.br',
                    'role': 'RESPONSIBLE'
                }
            ],
            'students': [
                {
                    'user_id': 1,
                    'name': 'VITOR GUIRAO SOLLER',
                    'email': '21.01444-2@maua.br',
                    'role': 'STUDENT'
                },
                {
                    'user_id': 2,
                    'name': 'JOAO VITOR CHOUERI BRANCO',
                    'email': '21.01075-7@maua.br',
                    'role': 'STUDENT'
                },
                {
                    'user_id': 3,
                    'name': 'BRUNO VILARDI BUENO',
                    'email': '19.00331-5@maua.br',
                    'role': 'STUDENT'
                }
            ]
        }

        task = {
            'task_id': 1,
            'title': 'Dados do Trabalho',
            'delivery_date': '2023-05-22',
            'responsible': 'STUDENT'
        }
       
        user = {
            'user_id': 3,
            'name': 'BRUNO VILARDI BUENO',
            'email': '19.00331-5@maua.br',
            'role': 'STUDENT'
        }
        len_before = len(repo.deliveries)
        repo.create_delivery(delivery=delivery, user=user, task=task, project=project)

        assert len(repo.deliveries) == len_before + 1

    def test_get_delivery(self):
        repo = DeliveryRepositoryMock()
        delivery = repo.get_delivery(1)
        assert delivery == repo.deliveries[0]

    def test_get_deliveries(self):
        repo = DeliveryRepositoryMock()
        deliveries = repo.get_deliveries(1)
        assert deliveries == repo.deliveries

