from abc import abstractmethod

from app.repos.repo_interface import RepoInterface


class ITaskRepository(RepoInterface):

    @abstractmethod
    def get_all_tasks(self):
        """
        Return all tasks, including the ones that are not completed.
        """
        pass
