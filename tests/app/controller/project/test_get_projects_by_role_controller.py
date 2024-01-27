from django.test import TestCase, RequestFactory

from app.controllers.project.get_projects_by_role_controller import GetProjectsByRoleController
from app.helpers.http.django_http_request import DjangoHttpRequest
from app.repos.project.project_repository_mock import ProjectRepositoryMock


class TestGetProjectsByRoleController(TestCase):

    def test_get_projects_by_role_controller(self):
        request = DjangoHttpRequest(
            request=None,
            data={
                "user_id": 1,
            },
            method="GET"
        )

        repo = ProjectRepositoryMock()
        controller = GetProjectsByRoleController(repo)
        response = controller(request)

        assert response.status_code == 200
        assert response.message == "The project were retrieved successfully"
        
    def test_get_projects_by_role_controller_missing_user_id(self):
        request = DjangoHttpRequest(
            request=None,
            data={
            },
            method="GET"
        )

        repo = ProjectRepositoryMock()
        controller = GetProjectsByRoleController(repo)
        response = controller(request)

        assert response.status_code == 400
        assert response.message == "Field user_id is missing for method get_projects_by_role"
        
    def test_get_projects_by_role_controller_missing_body(self):
        request = DjangoHttpRequest(
            request=None,
            data={
                "user_id": 1,
            },
            method="POST"
        )

        repo = ProjectRepositoryMock()
        controller = GetProjectsByRoleController(repo)
        response = controller(request)

        assert response.status_code == 400
        assert response.message == "Field body is missing for method get_projects_by_role"
        
    def test_get_projects_by_role_controller_wrong_type_user_id(self):
        request = DjangoHttpRequest(
            request=None,
            data={
                "user_id": "a",
            },
            method="GET"
        )

        repo = ProjectRepositoryMock()
        controller = GetProjectsByRoleController(repo)
        response = controller(request)

        assert response.status_code == 400
        assert response.message == "Tipo de parâmetro incorreto para user_id"
