from abc import abstractmethod

from app.models.repos.repo_interface import RepoInterface


class ProfessorRepoInterface(RepoInterface):
    def __init__(self):
        pass
    
    @abstractmethod
    def get_all_professors(self):
        pass