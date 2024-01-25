from app.models import User
from app.repos.user.user_repository_interface import IUserRepository


class UserRepositoryPostgres(IUserRepository):

    def __init__(self):
        pass

    def get_user(self, user_id: int):
        try:
            return User.objects.get(user_id=user_id).to_dict()
        except:
            return None