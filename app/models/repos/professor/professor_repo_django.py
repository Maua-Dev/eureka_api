from app.models.models import Professor
from app.models.repos.professor.professor_repo_interface import ProfessorRepoInterface


class ProfessorRepoDjango(ProfessorRepoInterface):
    
    def get_all_professors(self):
        return Professor.objects.all()