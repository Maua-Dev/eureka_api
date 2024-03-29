from django.test import TestCase, RequestFactory

from app.controllers.project.create_project_controller import CreateProjectController
from app.helpers.http.django_http_request import DjangoHttpRequest
from app.repos.project.project_repository_mock import ProjectRepositoryMock
from app.repos.user.user_repository_mock import UserRepositoryMock


class TestCreateProjectController(TestCase):

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

        project_repo = ProjectRepositoryMock()
        user_repo = UserRepositoryMock()
        controller = CreateProjectController(project_repo=project_repo, user_repo=user_repo)
        response = controller(request)

        assert response.status_code == 201
        assert response.body == {
            "project_id": len(project_repo.projects),
            "title": "Analisando a viabilidade de um sistema de monitoramento de idosos",
            "qualification": "Engenharia de Software",
            "code": "ES-01",
            "shift": "DIURNO",
            "stand_number": "1",
            "is_entrepreneurship": False,
            "professors": [3, 4],
            "students": []
        }
        
    def test_create_project_controller_student_not_found(self):
        user_repo = UserRepositoryMock()
        request = DjangoHttpRequest(
            request=None,
            data={
                "title": "Analisando a viabilidade de um sistema de monitoramento de idosos",
                "qualification": "Engenharia de Software",
                "code": "ES-01",
                "shift": "DIURNO",
                "stand_number": "1",
                "is_entrepreneurship": False,
                "professors": [3, 4],
                "students": [len(user_repo.users)+1]
            },
            method="POST"    
        )

        project_repo = ProjectRepositoryMock()
        controller = CreateProjectController(project_repo=project_repo, user_repo=user_repo)
        response = controller(request)

        assert response.status_code == 404
        assert response.message == "Usuário não encontrado"
        
    def test_create_project_controller_student_in_two_projects(self):
        user_repo = UserRepositoryMock()

        request = DjangoHttpRequest(
            request=None,
            data={
                "title": "Analisando a viabilidade de um sistema de monitoramento de idosos",
                "qualification": "Engenharia de Software",
                "code": "ES-01",
                "shift": "DIURNO",
                "stand_number": "1",
                "is_entrepreneurship": False,
                "professors": [3, 4],
                "students": [len(user_repo.users), 1]
            },
            method="POST"    
        )

        project_repo = ProjectRepositoryMock()
        controller = CreateProjectController(project_repo=project_repo, user_repo=user_repo)
        response = controller(request)

        assert response.message == "Estudante já cadastrado em um projeto"
        assert response.status_code == 403
        
    def test_create_project_controller_students_not_list(self):
        request = DjangoHttpRequest(
            request=None,
            data={
                "title": "Analisando a viabilidade de um sistema de monitoramento de idosos",
                "qualification": "Engenharia de Software",
                "code": "ES-01",
                "shift": "DIURNO",
                "stand_number": "1",
                "is_entrepreneurship": False,
                "professors": [3, 4],
                "students": (1,2,3)
            },
            method="POST"    
        )

        project_repo = ProjectRepositoryMock()
        user_repo = UserRepositoryMock()
        controller = CreateProjectController(project_repo=project_repo, user_repo=user_repo)
        response = controller(request)

        assert response.status_code == 400
        assert response.message == "Tipo de parâmetro incorreto para students"

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

        project_repo = ProjectRepositoryMock()
        user_repo = UserRepositoryMock()
        controller = CreateProjectController(project_repo=project_repo, user_repo=user_repo)
        response = controller(request)

        assert response.status_code == 400
        assert response.message == "Field title is missing for method create_project"



