from django.test import TestCase

from app.models import User, Project
from app.repos.project.project_repository_postgres import ProjectRepositoryPostgres


class TestProjectRepositoryPostgres(TestCase):

    def setUp(self):
        User.objects.create(user_id=1, name='VITOR GUIRAO SOLLER', email='21.01444-2@maua.br', role='STUDENT')
        User.objects.create(user_id=2, name='JOAO VITOR CHOUERI BRANCO', email='21.01075-7@maua.br', role='STUDENT')
        User.objects.create(user_id=3, name='BRUNO VILARDI BUENO', email='19.00331-5@maua.br', role='STUDENT')
        User.objects.create(user_id=4, name='CARLOS EDUARDO DANTAS DE MENEZES', email='carlos.menezes@maua.br', role='ADVISOR')
        User.objects.create(user_id=5, name='ANA PAULA GONCALVES SERRA', email='ana.serra@maua.br', role='RESPONSIBLE')
        project = Project.objects.create(title="Teste", qualification="Engenharia da Computação", code="ECOM000", shift="DIURNO", stand_number="1", is_entrepreneurship=False)
        project.professors.add(4, 5)
        project.students.add(1, 2, 3)
        project.save()

    def test_create_project(self):
        repo = ProjectRepositoryPostgres()
        project = {
            'title': "Estudo da Computação Quântica",
            'qualification': "Engenharia da Computação",
            'code': "ECOM000",
            'shift': "DIURNO",
            'stand_number': "1",
            'is_entrepreneurship': False,
            'students': [1, 2, 3],
            'professors': [4, 5],
        }

        count = Project.objects.count()

        repo.create_project(project)

        assert Project.objects.count() == count + 1

    def test_update_project(self):
        setUp(self)
        repo = ProjectRepositoryPostgres()

        project = {
            "project_id": 1,
            'title': "Teste2",
            'is_entrepreneurship': True,
        }

        repo.update_project(project)

        assert Project.objects.get(project_id=1).title == 'Teste2'
        assert Project.objects.get(project_id=1).is_entrepreneurship

    def test_get_project(self):
        repo = ProjectRepositoryPostgres()

        project = repo.get_project(1)

        assert project.title == 'Teste'
        assert project.is_entrepreneurship == False
