from app.models.repos.professor.professor_repo_interface import ProfessorRepoInterface


class ProfessorRepoMock(ProfessorRepoInterface):
    professors: str = []
    
    def __init__(self):
        self.professors = [
            {
                "professor_id": 1,
                "name": "Professor 1",
                "rf": "123456"
            },
            {
                "professor_id": 2,
                "name": "Professor 2",
                "rf": "654321"
            }
        ]
    
    def get_all_professors(self):
        return self.professors