from app.helpers.errors.base_error import BaseError


class MissingParameters(BaseError):
    def __init__(self, field: str, method: str):
        super().__init__(f'Field {field} is missing for method {method}')