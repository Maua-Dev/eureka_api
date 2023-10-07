from app.helpers.errors.base_error import BaseError


class ConflictInParameters(BaseError):
    def __init__(self, key: str, param1: str, param2: str, method: str):
        super().__init__(f'Key {key} is conflicting between parameters {param1} and {param2} in method {method}')