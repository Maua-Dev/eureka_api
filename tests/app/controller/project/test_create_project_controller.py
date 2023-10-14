from django.test import TestCase, RequestFactory

from app.controllers.project.create_project_controller import CreateController
from app.repos.project.project_repository_mock import ProjectRepositoryMock


class Test_GetAllTasksController(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_create_project_controller(self):
        request = self.factory.post('/create_project', {
            "title": "Analisando a viabilidade de um sistema de monitoramento de idosos",
            "qualification": "Engenharia de Software",
            "code": "ES-01",
            "shift": "DIURNO",
            "stand_number": "1",
        })

        request.POST.professors = [3, 4]
        request.POST.is_entrepreneurship = False

        repo = ProjectRepositoryMock()
        controller = CreateController(repo)
        response = controller(request)

        assert response.status_code == 200
        assert response.body == {
            "project_id": 1,
            "title": "Analisando a viabilidade de um sistema de monitoramento de idosos",
            "qualification": "Engenharia de Software",
            "code": "ES-01",
            "shift": "DIURNO",
            "stand_number": "1",
            "is_entrepreneurship": False,
            "professors": [3, 4],
            "students": []
        }

    def test_create_project_controller_missing_title(self):
        request = self.factory.post('/create_project', {
            "qualification": "Engenharia de Software",
            "code": "ES-01",
            "shift": "DIURNO",
            "stand_number": "1",
            "is_entrepreneurship": False,
            "professors": [3, 4]
        })

        repo = ProjectRepositoryMock()
        controller = CreateController(repo)
        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field title is missing for method create_project"




