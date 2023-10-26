from app.controllers.controller_interface import IController
from app.helpers.http.http_codes import InternalServerError, OK

class GetAllUsersController(IController):
    def __init__(self, repo):
        super().__init__(repo)
        self.repo = repo

    def __call__(self, request):
        try:
            self.error_handling(request)
            response_data = self.business_logic(request)

            return OK(
                body=[user.to_dict() for user in response_data] if type(response_data[0]) != dict else response_data,
                message="All users were successfully retrieved"
            )
            
        except Exception as err:
            return InternalServerError(
                message=str(err)
            )

    def error_handling(self, request):
        pass

    def business_logic(self, request):
        return self.repo.get_all_users()