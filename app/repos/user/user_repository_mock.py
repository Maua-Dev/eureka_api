from typing import Dict, List

from app.enums.user_role_enum import USER_ROLE
from app.repos.user.user_repository_interface import IUserRepository


class UserRepositoryMock(IUserRepository):
    users: List[Dict[str, str]]

    def __init__(self):
        self.users = [
            {
                "user_id": 1,
                "name": "Vitor Soller"
            }
        ]

    def get_user(self, user_id: int):
        for user in self.users:
            if user['user_id'] == user_id:
                return user
        return None