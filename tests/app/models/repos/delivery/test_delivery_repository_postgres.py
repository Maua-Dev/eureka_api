from django.test import TestCase

from app.models import Delivery, Task, Project, User
from app.repos.delivery.delivery_repository_postgres import DeliveryRepositoryPostgres


class Test_DeliveryRepositoryPostgres(TestCase):
    @classmethod
    def setUpTestData(cls):
        Task.objects.create(task_id=1, title="Dados do Trabalho", delivery_date="2023-05-22", responsible="STUDENT")
        Task.objects.create(task_id=2, title="Dados do Trabalho", delivery_date="2023-09-14", responsible="RESPONSIBLE")

        User.objects.create(user_id=1, name='VITOR GUIRAO SOLLER', email='21.01444-2@maua.br', role='STUDENT')
        User.objects.create(user_id=2, name='JOAO VITOR CHOUERI BRANCO', email='21.01075-7@maua.br', role='STUDENT')
        User.objects.create(user_id=3, name='BRUNO VILARDI BUENO', email='19.00331-5@maua.br', role='STUDENT')
        User.objects.create(user_id=4, name='CARLOS EDUARDO DANTAS DE MENEZES', email='carlos.menezes@maua.br',
                            role='ADVISOR')
        User.objects.create(user_id=5, name='ANA PAULA GONCALVES SERRA', email='ana.serra@maua.br', role='RESPONSIBLE')

        project = Project.objects.create(title="Teste", qualification="Engenharia da Computação", code="ECOM000",
                                         shift="DIURNO", stand_number="1", is_entrepreneurship=False)
        project.professors.add(4, 5)
        project.students.add(1, 2, 3)
        project.save()

    def test_create_delivery(self):
        repo = DeliveryRepositoryPostgres()
        delivery = {
            "task": 1,
            "project": 1,
            "user": 3,
            "content": "Algum conteúdo",
        }

        delivery_expected = {
            'delivery_id': 1,
            'task': {
                'task_id': 1,
                'title': 'Dados do Trabalho',
                'delivery_date': '2023-05-22',
                'responsible': 'STUDENT'
            },
            'project': {
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
            },
            'user': {
                'user_id': 3,
                'name': 'BRUNO VILARDI BUENO',
                'email': '19.00331-5@maua.br',
                'role': 'STUDENT'
            },
            'content': 'Algum conteúdo'
        }
        len_before = Delivery.objects.count()

        delivery_created = repo.create_delivery(delivery)
        len_after = Delivery.objects.count()

        assert len_after == len_before + 1
        assert delivery_created.to_dict() == delivery_expected

    def test_create_delivery_invalid_task(self):
        repo = DeliveryRepositoryPostgres()
        delivery = {
            "task": 3,
            "project": 1,
            "user": 3,
            "content": "Algum conteúdo",
        }

        delivery_created = repo.create_delivery(delivery)

        assert delivery_created is None
