from django.test import TestCase
from app.repos.task.task_repository_mock import TaskRepositoryMock


class TestTaskRepositoryMock(TestCase):
    def test_get_all_tasks(self):
        repo = TaskRepositoryMock()
        tasks = repo.get_all_tasks()
        assert tasks == repo.tasks
        
    def test_get_task(self):
        repo = TaskRepositoryMock()
        task = repo.get_task(1)
        assert task == repo.tasks[0]
        
    def test_get_task_not_found(self):
        repo = TaskRepositoryMock()
        task = repo.get_task(100)
        assert task is None
