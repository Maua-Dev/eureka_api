import datetime

from django.test import TestCase

from app.models import Task
from app.repos.task.task_repository_postgres import TaskRepositoryPostgres


class TestTaskRepositoryPostgres(TestCase):
    @classmethod
    def setUpTestData(cls):
        Task.objects.create(task_id=0, title="Delivery 1", delivery_date="2023-05-15", responsible="STUDENT")
        Task.objects.create(task_id=1, title="Delivery 1", delivery_date="2023-05-22", responsible="ADVISOR")
        Task.objects.create(task_id=2, title="Delivery 1", delivery_date="2023-09-14", responsible="RESPONSIBLE")
        Task.objects.create(task_id=3, title="Delivery 2", delivery_date="2023-10-01", responsible="STUDENT")
        Task.objects.create(task_id=4, title="Delivery 2", delivery_date="2023-10-03", responsible="ADVISOR")

    def test_get_all_tasks(self):
        repo = TaskRepositoryPostgres()
        tasks = repo.get_all_tasks()
        assert len(tasks) == 5
        assert tasks[0].task_id == 0
        assert tasks[0].title == "Delivery 1"
        assert tasks[0].delivery_date == datetime.date(2023, 5, 15)
        assert tasks[0].responsible == "STUDENT"

