from abc import abstractmethod

from app.repos.repo_interface import RepoInterface


class IDeliveryRepository(RepoInterface):

    @abstractmethod
    def create_delivery(self, delivery: dict, user: dict, task: dict, project: dict):
        pass

    @abstractmethod
    def get_delivery(self, delivery_id: dict):
        pass

    @abstractmethod
    def get_deliveries(self, project_id: dict):
        pass






