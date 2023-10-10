from typing import Dict, List

from app.enums.user_role_enum import USER_ROLE
from app.repos.task.task_repository_interface import ITaskRepository


class TaskRepositoryMock(ITaskRepository):
    tasks: List[Dict[str, str]]

    def __init__(self):
        self.tasks = [
            {
                "task_id": 1,
                "name": "Dados do trabalho",
                "delivery_date": "15/05/2023",
                "responsible": USER_ROLE.STUDENT.value
            },
            {
                "task_id": 2,
                "name": "Dados do trabalho",
                "delivery_date": "22/05/2023",
                "responsible": USER_ROLE.ADVISOR.value
            },
            {
                "task_id": 3,
                "name": "Dados do trabalho",
                "delivery_date": "14/09/2023",
                "responsible": USER_ROLE.RESPONSIBLE.value
            },
            {
                "task_id": 4,
                "name": "Pôster Técnico (PDF)",
                "delivery_date": "01/10/2023",
                "responsible": USER_ROLE.STUDENT.value
            },
            {
                "task_id": 5,
                "name": "Pôster Técnico (PDF)",
                "delivery_date": "03/10/2023",
                "responsible": USER_ROLE.ADVISOR.value
            },
            {
                "task_id": 6,
                "name": "Pôster Imagem",
                "delivery_date": "17/09/2023",
                "responsible": USER_ROLE.STUDENT.value
            },
            {
                "task_id": 7,
                "name": "Pôster Imagem",
                "delivery_date": "20/09/2023",
                "responsible": USER_ROLE.ADVISOR.value
            },
        ]

    def get_all_tasks(self):
        return self.tasks
