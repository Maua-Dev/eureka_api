from app.controllers.delivery.get_deliveries_controller import GetDeliveriesController
from app.environments import Environments
from app.controllers.delivery.create_delivery_controller import CreateDeliveryController
from app.helpers.http.django_http_request import DjangoHttpRequest
from app.helpers.http.django_http_response import DjangoHttpResponse

delivery_repo = Environments.get_delivery_repo()()
task_repo = Environments.get_task_repo()()
project_repo = Environments.get_project_repo()()
user_repo = Environments.get_user_repo()()

class DeliveryViews:

    @staticmethod
    def create_delivery(request):
        controller = CreateDeliveryController(repo)
        http_request = DjangoHttpRequest(request)
        response = controller(http_request)
        http_response = DjangoHttpResponse(body=response.body, status_code=response.status_code,
                                           message=response.message)

        return http_response.to_django()


    @staticmethod
    def get_deliveries(request):
        controller = GetDeliveriesController(repo)
        http_request = DjangoHttpRequest(request)
        response = controller(http_request)
        http_response = DjangoHttpResponse(body=response.body, status_code=response.status_code,
                                           message=response.message)

        return http_response.to_django()
