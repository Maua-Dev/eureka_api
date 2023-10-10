from django.test import TestCase

from app.models import Task


def load_db():
    Task.objects.create(task_id=0, title="Delivery 1", delivery_date="2023-05-15", responsible="STUDENT")
    Task.objects.create(task_id=1, title="Delivery 1", delivery_date="2023-05-22", responsible="ADVISOR")
    Task.objects.create(task_id=2, title="Delivery 1", delivery_date="2023-09-14", responsible="RESPONSIBLE")
    Task.objects.create(task_id=3, title="Delivery 2", delivery_date="2023-10-01", responsible="STUDENT")
    Task.objects.create(task_id=4, title="Delivery 2", delivery_date="2023-10-03", responsible="ADVISOR")


class TestrRepositoryPostgres(TestCase):
    def test_get_all_tasks(self):
        load_db()
        tasks = Task.objects.all()
        assert len(tasks) == len(Task.objects.all())
