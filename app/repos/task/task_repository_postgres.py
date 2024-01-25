from app.models import Task
from app.repos.task.task_repository_interface import ITaskRepository


class TaskRepositoryPostgres(ITaskRepository):

    def __init__(self):
        pass

    def get_all_tasks(self):
        return Task.objects.all()

    def get_task(self, task_id: int):
        try:
            return Task.objects.get(task_id=task_id).to_dict()
        except:
            return None