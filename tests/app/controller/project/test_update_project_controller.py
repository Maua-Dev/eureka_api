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
            method="PUT"
        )

        repo = ProjectRepositoryMock()
        controller = UpdateProjectController(repo)
        response = controller(request)

        assert response.status_code == 200
        assert response.body['title'] == 'Estudando Computação Quântica'

    def test_update_project_controller_missing_project_id(self):
        request = DjangoHttpRequest(
            request=None,
            data={
                "title": "None",
            },
            method="PUT"
        )

        repo = ProjectRepositoryMock()
        controller = UpdateProjectController(repo)
        response = controller(request)

        assert response.status_code == 400
        assert response.message == "Field project_id is missing for method update_project"

    def test_update_project_controller_not_found_project_id(self):
        request = DjangoHttpRequest(
            request=None,
            data={
                "project_id": 1000,
                "title": "Estudando Computação Quântica",
            },
            method="PUT"
        )

        repo = ProjectRepositoryMock()
        controller = UpdateProjectController(repo)
        response = controller(request)

        assert response.status_code == 404
        assert response.message == "Projeto não encontrado"



