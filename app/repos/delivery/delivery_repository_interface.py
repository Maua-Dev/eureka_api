from abc import abstractmethod

from app.repos.repo_interface import RepoInterface


class IDeliveryRepository(RepoInterface):

    @abstractmethod
    def create_delivery(self, delivery):
        pass


