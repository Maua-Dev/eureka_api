from django.test import TestCase, RequestFactory

from app.controllers.user.get_all_users_controller import GetAllUsersController
from app.repos.user.user_repository_mock import UserRepositoryMock

class TestGetAllUsersController(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_get_all_users_controller(self):
        request = self.factory.get('/get_all_users')
        repo = UserRepositoryMock()
        controller = GetAllUsersController(repo)
        response = controller(request)

        assert response.status_code == 200
        assert response.message == "All users were successfully retrieved"
        assert len(response.body) == len(repo.users)
        assert response.body[0]['user_id'] == repo.users[0]['user_id']
        assert response.body[0]['name'] == repo.users[0]['name']
        assert response.body[0]['email'] == repo.users[0]['email']
        assert response.body[0]['role'] == repo.users[0]['role']