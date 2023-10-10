from app.repos.professor.professor_repo_django import ProfessorRepoDjango
from app.models.models import Professor
from django.test import TestCase

def load_db():
    Professor.objects.create(professor_id=0, name="Joao Branco", rf="ABC")
    Professor.objects.create(professor_id=2, name="Joao Branco 2" , rf="2BC")


class TestProfessorRepoDjango(TestCase):
    def test_get_all_professors(self):
        load_db()
        repo = ProfessorRepoDjango()
        professors = repo.get_all_professors()
        assert len(professors) == len(Professor.objects.all())
