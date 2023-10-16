from django.test import TestCase, RequestFactory

from app.controllers.project.create_project_controller import CreateProjectController
from app.helpers.http.django_http_request import DjangoHttpRequest
from app.repos.project.project_repository_mock import ProjectRepositoryMock


class TestCreateProjectController(TestCase):

    # def setUp(self):
    #     self.factory = RequestFactory()


    def test_create_project_controller(self):
        request = DjangoHttpRequest(
            request=None,
            data={
                "title": "Analisando a viabilidade de um sistema de monitoramento de idosos",
                "qualification": "Engenharia de Software",
                "code": "ES-01",
                "shift": "DIURNO",
                "stand_number": "1",
                "is_entrepreneurship": False,
                "professors": [3, 4]
            },
            method="POST"    
        )

        repo = ProjectRepositoryMock()
        controller = CreateProjectController(repo)
        response = controller(request)

        assert response.status_code == 201
        assert response.body == {
            "project_id": 2,
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
        request = DjangoHttpRequest(
            request=None,
            data={
                "title": None,
                "qualification": "Engenharia de Software",
                "code": "ES-01",
                "shift": "DIURNO",
                "stand_number": "1",
                "is_entrepreneurship": False,
                "professors": [3, 4]
            },
            method="POST"    
        )

        repo = ProjectRepositoryMock()
        controller = CreateProjectController(repo)
        response = controller(request)

        assert response.status_code == 400
        assert response.message == "Field title is missing for method create_project"



