from app.models import Task
from app.repos.task.task_repository_interface import ITaskRepository


class TaskRepositoryPostgres(ITaskRepository):

    def __init__(self):
        pass

    def get_all_tasks(self):
        return Task.objects.all()
