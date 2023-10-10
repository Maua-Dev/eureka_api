import os
from enum import Enum
from typing import Type

from app.models.repos.professor.professor_repo_interface import ProfessorRepoInterface
from app.models.repos.professor.professor_repo_mock import ProfessorRepoMock


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
        os.environ["STAGE"] = os.environ.get("STAGE") or STAGE.DOTENV.value

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
    def get_professor_repo() -> Type[ProfessorRepoMock]:
        if Environments.get_envs().stage == STAGE.TEST:
            from app.models.repos.professor.professor_repo_mock import ProfessorRepoMock
            return ProfessorRepoMock
        # ELIF TO OTHER STAGES

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
