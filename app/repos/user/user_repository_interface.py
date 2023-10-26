from abc import abstractmethod
from app.repos.repo_interface import RepoInterface

class IUserRepository(RepoInterface):
    
    @abstractmethod
    def get_all_users(self):
        """
        Returns all users.
        """
        pass