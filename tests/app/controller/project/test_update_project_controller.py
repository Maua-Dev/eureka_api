from django.test import TestCase, RequestFactory

from app.controllers.project.update_project_controller import UpdateProjectController
from app.helpers.http.django_http_request import DjangoHttpRequest
from app.repos.project.project_repository_mock import ProjectRepositoryMock


class TestUpdateProjectController(TestCase):

    def test_update_project_controller(self):
        request = DjangoHttpRequest(
            request=None,
            data={
                "project_id": 1,
                "title": "Estudando Computação Quântica",
            },
            method="POST"    
        )

        repo = ProjectRepositoryMock()
        controller = UpdateProjectController(repo)
        response = controller(request)

        assert response.status_code == 200
        assert response.body == {'code': 'ECOM000', 'is_entrepreneurship': False, 'professors': [1, 2, 3], 'project_id': 1, 'qualification': 'Engenharia da Computação', 'shift': 'DIRUNO', 'stand_number': '1', 'students': [4, 5], 'title': 'Estudando Computação Quântica'}

    def test_update_project_controller_missing_project_id(self):
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
        controller = UpdateProjectController(repo)
        response = controller(request)

        assert response.status_code == 400
        assert response.message == "Field project_id is missing for method update_project"





