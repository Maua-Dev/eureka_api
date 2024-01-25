from typing import Dict, List

from app.enums.user_role_enum import USER_ROLE
from app.repos.task.task_repository_interface import ITaskRepository


class TaskRepositoryMock(ITaskRepository):
    tasks: List[Dict[str, str]]

    def __init__(self):
        self.tasks = [
            {
                "task_id": 1,
                "title": "Dados do trabalho",
                "delivery_date": "2023-05-15",
                "responsible": USER_ROLE.STUDENT.value
            },
            {
                "task_id": 2,
                "title": "Dados do trabalho",
                "delivery_date": "2023-05-22",
                "responsible": USER_ROLE.ADVISOR.value
            },
            {
                "task_id": 3,
                "title": "Dados do trabalho",
                "delivery_date": "2023-09-14",
                "responsible": USER_ROLE.RESPONSIBLE.value
            },
            {
                "task_id": 4,
                "title": "Pôster Técnico (PDF)",
                "delivery_date": "2023-10-01",
                "responsible": USER_ROLE.STUDENT.value
            },
            {
                "task_id": 5,
                "title": "Pôster Técnico (PDF)",
                "delivery_date": "2023-10-03",
                "responsible": USER_ROLE.ADVISOR.value
            },
            {
                "task_id": 6,
                "title": "Pôster Imagem",
                "delivery_date": "2023-09-17",
                "responsible": USER_ROLE.STUDENT.value
            },
            {
                "task_id": 7,
                "title": "Pôster Imagem",
                "delivery_date": "2023-09-20",
                "responsible": USER_ROLE.ADVISOR.value
            },
        ]

    def get_all_tasks(self):
        return self.tasks

    def get_task(self, task_id: int):
        for task in self.tasks:
            if task['task_id'] == task_id:
                return task
        return None