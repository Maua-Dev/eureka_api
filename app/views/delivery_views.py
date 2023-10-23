from app.environments import Environments
from app.controllers.delivery.create_delivery_controller import CreateDeliveryController
from app.helpers.http.django_http_request import DjangoHttpRequest
from app.helpers.http.django_http_response import DjangoHttpResponse

repo = Environments.get_delivery_repo()()


class DeliveryViews:

    @staticmethod
    def create_delivery(request):
        controller = CreateDeliveryController(repo)
        http_request = DjangoHttpRequest(request)
        response = controller(http_request)
        http_response = DjangoHttpResponse(body=response.body, status_code=response.status_code,
                                           message=response.message)

        return http_response.to_django()
