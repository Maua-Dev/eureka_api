from django.test import TestCase
from app.repos.task.task_repository_mock import TaskRepositoryMock


class TestTaskRepositoryMock(TestCase):
    def test_get_all_tasks(self):
        repo = TaskRepositoryMock()
        tasks = repo.get_all_tasks()
        assert tasks == repo.tasks
