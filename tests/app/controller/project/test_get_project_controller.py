from django.test import TestCase, RequestFactory

from app.controllers.project.get_project_controller import GetProjectController
from app.helpers.http.django_http_request import DjangoHttpRequest
from app.repos.project.project_repository_mock import ProjectRepositoryMock


class TestGetProjectController(TestCase):

    def test_get_project_controller(self):
        request = DjangoHttpRequest(
            request=None,
            data={
                "project_id": 1,
            },
            method="GET"
        )

        repo = ProjectRepositoryMock()
        controller = GetProjectController(repo)
        response = controller(request)

        assert response.status_code == 200
        assert response.message == "The project was retrieved"

    def test_get_project_controller_missing_project_id(self):
        request = DjangoHttpRequest(
            request=None,
            data={

            },
            method="GET"
        )

        repo = ProjectRepositoryMock()
        controller = GetProjectController(repo)
        response = controller(request)

        assert response.status_code == 400
        assert response.message == "Field project_id is missing for method get_project"

    def test_get_project_controller_not_found(self):
        request = DjangoHttpRequest(
            request=None,
            data={
                "project_id": 2,
            },
            method="GET"
        )

        repo = ProjectRepositoryMock()
        controller = GetProjectController(repo)
        response = controller(request)

        assert response.status_code == 404
        assert response.message == "Projeto não encontrado"


    def test_get_project_controller_wrong_type(self):
        request = DjangoHttpRequest(
            request=None,
            data={
                "project_id": "batata",
            },
            method="GET"
        )

        repo = ProjectRepositoryMock()
        controller = GetProjectController(repo)
        response = controller(request)

        assert response.message == "Tipo de parâmetro incorreto para project_id"
        assert response.status_code == 400

