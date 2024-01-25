from app.helpers.errors.base_error import BaseError


class MissingParameters(BaseError):
    def __init__(self, field: str, method: str):
        super().__init__(f'Field {field} is missing for method {method}')
        
        
class NotFound(BaseError):
    def __init__(self, model: str, genre: str = 'o'):
        super().__init__(f'{model} não encontrad{genre}')
        
class ProjectNotFound(NotFound):
    def __init__(self):
        super().__init__(model='Projeto')
        
class TaskNotFound(NotFound):
    def __init__(self):
        super().__init__(model='Tarefa', genre='a')
        
class DeliveryNotFound(NotFound):
    def __init__(self):
        super().__init__(model='Entrega', genre='a')