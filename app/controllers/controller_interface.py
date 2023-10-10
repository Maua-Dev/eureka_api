from abc import abstractmethod
from app.helpers.http.http_models import HttpRequestModel
from app.repos.repo_interface import RepoInterface 


class IController:
    def __init__(self, repo: RepoInterface):
        self.repo = repo
        
    @abstractmethod
    def __call__(self, request: HttpRequestModel):
        pass
    
    @abstractmethod
    def error_handling(self, request: HttpRequestModel):
        pass
    
    @abstractmethod
    def business_logic(self, request: HttpRequestModel):
        pass
