from typing import Dict, List
from app.enums.user_role_enum import USER_ROLE
from app.repos.user.user_repository_interface import IUserRepository

class UserRepositoryMock(IUserRepository):
    users = List[Dict[str, str]]
    
    def __init__(self):
        self.users = [
            {
                "user_id": 1,
                "name" : "Luigi Trevisan",
                "email" : "22.01102-0@maua.br",
                "role" : USER_ROLE.STUDENT.value
            },
            {
                "user_id": 2,
                "name" : "João Branco",
                "email" : "21.01094-2@maua.br",
                "role" : USER_ROLE.STUDENT.value
            },
            {
                "user_id": 3,
                "name" : "Everson Dênis",
                "email" : "everson@maua.br",
                "role" : USER_ROLE.ADVISOR.value
            },
            {
                "user_id": 4,
                "name" : "Ricardo Balistiero",
                "email" : "balistiero@maua.br",
                "role" : USER_ROLE.RESPONSIBLE.value
            }
        ]
        
    def get_all_users(self):
        return self.users