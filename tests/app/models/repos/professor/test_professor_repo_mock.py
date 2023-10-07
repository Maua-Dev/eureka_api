from app.models.repos.professor.professor_repo_mock import ProfessorRepoMock


class TestProfessorRepoMock:
    def test_get_all_professors(self):
        repo = ProfessorRepoMock()
        professors = repo.get_all_professors()
        assert professors == repo.professors