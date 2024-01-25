from abc import abstractmethod
from typing import Dict, List

from app.repos.repo_interface import RepoInterface


class ITaskRepository(RepoInterface):

    @abstractmethod
    def get_all_tasks(self) -> List[Dict[str, str]]:
        """
        Return all tasks, including the ones that are not completed.
        """
        pass

    @abstractmethod
    def get_task(self, task_id) -> Dict[str, str]:
        """
        Return task by task_id.
        """
        pass