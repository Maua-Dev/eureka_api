from abc import abstractmethod

from app.repos.repo_interface import RepoInterface


class IProjectRepository(RepoInterface):

    @abstractmethod
    def get_project(self, project_id: int):
        pass

    @abstractmethod
    def create_project(self, project):
        pass

    @abstractmethod
    def update_project(self, project):
        pass

    @abstractmethod
    def get_projects_by_role(self, user_id: int):
        pass


