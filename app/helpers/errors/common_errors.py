from app.helpers.errors.base_error import BaseError


class MissingParameters(BaseError):
    def __init__(self, field: str, method: str):
        super().__init__(f'Field {field} is missing for method {method}')
        


class ObjectNotFound(BaseError):
    def __init__(self, model: str, genre: str = 'o'):
        super().__init__(f'{model} não encontrad{genre}')
        
class RequestNotFound(ObjectNotFound):
    def __init__(self):
        super().__init__(model='Requisição', genre='a')
        
class ProjectNotFound(ObjectNotFound):
    def __init__(self):
        super().__init__(model='Projeto')
        
class TaskNotFound(ObjectNotFound):
    def __init__(self):
        super().__init__(model='Tarefa', genre='a')
        
class DeliveryNotFound(ObjectNotFound):
    def __init__(self):
        super().__init__(model='Entrega', genre='a')
        
class UserNotFound(ObjectNotFound):
    def __init__(self):
        super().__init__(model='Usuário', genre='o')

class RoleForbiddenAction(BaseError):
    def __init__(self, role: str):
        super().__init__(f'{role} não tem permissão para realizar esta ação')

class AdvisorForbiddenAction(RoleForbiddenAction):
    def __init__(self):
        super().__init__(role='Orientador')
        
class StudentForbiddenAction(RoleForbiddenAction):
    def __init__(self):
        super().__init__(role='Estudante')