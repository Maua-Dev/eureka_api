from app.models.repos.professor.professor_repo_mock import ProfessorRepoMock
from django.test import TestCase

class TestProfessorRepoMock(TestCase):
    def test_get_all_professors(self):
        repo = ProfessorRepoMock()
        professors = repo.get_all_professors()
        assert professors == repo.professors
