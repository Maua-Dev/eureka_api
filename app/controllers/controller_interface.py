from abc import abstractmethod
from app.helpers.http.http_models import HttpRequestModel
from app.repos.delivery.delivery_repository_interface import IDeliveryRepository
from app.repos.project.project_repository_interface import IProjectRepository
from app.repos.repo_interface import RepoInterface
from app.repos.task.task_repository_interface import ITaskRepository
from app.repos.user.user_repository_interface import IUserRepository 


class IController:
    def __init__(self, repo: RepoInterface=None, delivery_repo: IDeliveryRepository=None, task_repo: ITaskRepository=None, project_repo: IProjectRepository=None, user_repo: IUserRepository=None):
        self.repo = repo
        self.delivery_repo = delivery_repo
        self.task_repo = task_repo
        self.project_repo = project_repo
        self.user_repo = user_repo
        
    @abstractmethod
    def __call__(self, request: HttpRequestModel):
        pass
    
    @abstractmethod
    def error_handling(self, request: HttpRequestModel):
        pass
    
    @abstractmethod
    def business_logic(self, request: HttpRequestModel):
        pass
    
