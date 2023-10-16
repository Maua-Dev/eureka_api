from django.test import TestCase, RequestFactory

from app.controllers.task.get_all_tasks_controller import GetAllTasksController
from app.repos.task.task_repository_mock import TaskRepositoryMock


class TestGetAllTasksController(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_get_all_tasks_controller(self):
        request = self.factory.get('/get_all_tasks')
        repo = TaskRepositoryMock()
        controller = GetAllTasksController(repo)
        response = controller(request)

        assert response.status_code == 200
        assert response.message == "All tasks were successfully retrieved"
        assert len(response.body) == len(repo.tasks)
        assert response.body[0]['task_id'] == repo.tasks[0]['task_id']
        assert response.body[0]['title'] == repo.tasks[0]['title']
        assert response.body[0]['delivery_date'] == repo.tasks[0]['delivery_date']
        assert response.body[0]['responsible'] == repo.tasks[0]['responsible']
