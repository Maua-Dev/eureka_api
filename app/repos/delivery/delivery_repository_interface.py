from abc import abstractmethod

from app.repos.repo_interface import RepoInterface


class IDeliveryRepository(RepoInterface):

    @abstractmethod
    def create_delivery(self, delivery):
        pass

    @abstractmethod
    def get_delivery(self, delivery_id):
        pass

    @abstractmethod
    def get_deliveries(self, project_id):
        pass






