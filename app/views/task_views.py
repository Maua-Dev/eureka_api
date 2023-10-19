from app.controllers.task.get_all_tasks_controller import GetAllTasksController
from app.environments import Environments
from app.helpers.http.django_http_request import DjangoHttpRequest
from app.helpers.http.django_http_response import DjangoHttpResponse

repo = Environments.get_task_repo()()


class TaskViews:
    @staticmethod
    def get_all_tasks(request):
        controller = GetAllTasksController(repo)
        http_request = DjangoHttpRequest(request)
        response = controller(http_request)
        http_response = DjangoHttpResponse(body=response.body, status_code=response.status_code,
                                           message=response.message)

        return http_response.to_django()
