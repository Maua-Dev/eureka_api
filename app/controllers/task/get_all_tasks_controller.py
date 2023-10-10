from app.controllers.controller_interface import IController
from app.helpers.http.django_http_request import DjangoHttpRequest
from app.helpers.http.http_codes import InternalServerError, OK
from app.repos.task.task_repository_interface import ITaskRepository


class GetAllTasksController(IController):
    def __init__(self, repo: ITaskRepository):
        super().__init__(repo)
        self.repo = repo

    def __call__(self, request: DjangoHttpRequest):
        try:
            self.error_handling(request)
            response_data = self.business_logic(request)

            return OK(
                body=response_data,
                message="All tasks were successfully retrieved"
            )

        except Exception as err:
            return InternalServerError(
                message=str(err)
            )

    def error_handling(self, request: DjangoHttpRequest):
        pass

    def business_logic(self, request: DjangoHttpRequest):
        return self.repo.get_all_tasks()
