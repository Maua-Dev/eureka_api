from app.helpers.errors.base_error import BaseError


class MissingParameters(BaseError):
    def __init__(self, field: str, method: str):
        super().__init__(f'Field {field} is missing for method {method}')
        
        
class DataNotFound(BaseError):
    def __init__(self, model: str, genre: str = 'o'):
        super().__init__(f'{model} não encontrad{genre}')
        
class ProjectNotFound(DataNotFound):
    def __init__(self):
        super().__init__(model='Projeto')
        
class TaskNotFound(DataNotFound):
    def __init__(self):
        super().__init__(model='Tarefa', genre='a')
        
class DeliveryNotFound(DataNotFound):
    def __init__(self):
        super().__init__(model='Entrega', genre='a')
        
class UserNotFound(DataNotFound):
    def __init__(self):
        super().__init__(model='Usuário', genre='o')

class ForbiddenAction(BaseError):
    def __init__(self, role: str):
        super().__init__(f'{role} não tem permissão para realizar esta ação')

class AdvisorForbiddenAction(ForbiddenAction):
    def __init__(self):
        super().__init__(role='Orientador')
        
class StudentForbiddenAction(ForbiddenAction):
    def __init__(self):
        super().__init__(role='Estudante')