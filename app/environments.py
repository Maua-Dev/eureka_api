import os
from enum import Enum
from typing import Type

from app.repos.delivery.delivery_repository_interface import IDeliveryRepository
from app.repos.project.project_repository_interface import IProjectRepository


from app.repos.task.task_repository_interface import ITaskRepository
from app.repos.user.user_repository_interface import IUserRepository


class STAGE(Enum):
    DOTENV = "DOTENV"
    DEV = "DEV"
    HOMOLOG = "HOMOLOG"
    PROD = "PROD"
    TEST = "TEST"


class Environments:
    """
    Defines the environment variables for the application. You should not instantiate this class directly. Please use Environments.get_envs() method instead.

    Usage:

    """
    stage: STAGE

    def _configure_local(self):
        from dotenv import load_dotenv
        load_dotenv()
        if "STAGE" not in os.environ:
            os.environ["STAGE"] = STAGE.TEST.value

    def load_envs(self):
        if "STAGE" not in os.environ or os.environ["STAGE"] == STAGE.DOTENV.value:
            self._configure_local()

        self.stage = STAGE[os.environ.get("STAGE")]

        # ADD OTHER ENVIRONMENT VARIABLES HERE
        # if self.stage == STAGE.TEST:
        #
        #
        # else:

    @staticmethod
    def get_task_repo() -> Type[ITaskRepository]:
        if Environments.get_envs().stage == STAGE.TEST:
            from app.repos.task.task_repository_mock import TaskRepositoryMock
            return TaskRepositoryMock

        elif Environments.get_envs().stage in [STAGE.DEV, STAGE.HOMOLOG, STAGE.PROD]:
            from app.repos.task.task_repository_postgres import TaskRepositoryPostgres
            return TaskRepositoryPostgres

        else:
            raise Exception("No repository found for this stage")
        
    @staticmethod
    def get_project_repo() -> Type[IProjectRepository]:
        if Environments.get_envs().stage == STAGE.TEST:
            from app.repos.project.project_repository_mock import ProjectRepositoryMock
            return ProjectRepositoryMock

        elif Environments.get_envs().stage in [STAGE.DEV, STAGE.HOMOLOG, STAGE.PROD]:
            from app.repos.project.project_repository_postgres import ProjectRepositoryPostgres
            return ProjectRepositoryPostgres

        else:
            raise Exception("No repository found for this stage")

    @staticmethod
    def get_delivery_repo() -> Type[IDeliveryRepository]:
        if Environments.get_envs().stage == STAGE.TEST:
            from app.repos.delivery.delivery_repository_mock import DeliveryRepositoryMock
            return DeliveryRepositoryMock

        elif Environments.get_envs().stage in [STAGE.DEV, STAGE.HOMOLOG, STAGE.PROD]:
            from app.repos.delivery.delivery_repository_postgres import DeliveryRepositoryPostgres
            return DeliveryRepositoryPostgres

        else:
            raise Exception("No repository found for this stage")
    
    @staticmethod
    def get_user_repo() -> Type[IUserRepository]:
        if Environments.get_envs().stage == STAGE.TEST:
            # from app.repos.user.user_repository_postgres import UserRepositoryPostgres
            # return UserRepositoryPostgres
            from app.repos.user.user_repository_mock import UserRepositoryMock
            return UserRepositoryMock

        elif Environments.get_envs().stage in [STAGE.DEV, STAGE.HOMOLOG, STAGE.PROD]:
            from app.repos.user.user_repository_postgres import UserRepositoryPostgres
            return UserRepositoryPostgres

        else:
            raise Exception("No repository found for this stage")


    @staticmethod
    def get_envs() -> "Environments":
        """
        Returns the Environments object. This method should be used to get the Environments object instead of instantiating it directly.
        :return: Environments (stage={self.stage}, s3_bucket_name={self.s3_bucket_name}, region={self.region}, endpoint_url={self.endpoint_url})

        """
        envs = Environments()
        envs.load_envs()
        return envs

    def __repr__(self):
        return self.__dict__
