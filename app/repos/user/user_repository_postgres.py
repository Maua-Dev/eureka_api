from app.models.user import User
from app.repos.user.user_repository_interface import IUserRepository


class UserRepositoryPostgres(IUserRepository):
    
    def __init__(self):
        pass
    
    def get_all_users(self):
        return User.objects.all()