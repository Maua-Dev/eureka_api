from abc import abstractmethod

from app.repos.repo_interface import RepoInterface


class IUserRepository(RepoInterface):

    @abstractmethod
    def get_user(self):
        """
        Return user by user_id.
        """
        pass
