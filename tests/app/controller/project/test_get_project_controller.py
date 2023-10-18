from django.test import TestCase, RequestFactory

from app.controllers.project.get_project_controller import GetProjectController
from app.helpers.http.django_http_request import DjangoHttpRequest
from app.repos.project.project_repository_mock import ProjectRepositoryMock


class TestGetProjectController(TestCase):

    def test_update_project_controller(self):
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

    def test_update_project_controller_missing_project_id(self):
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
        assert response.message == "Field project_id is missing for method update_project"





