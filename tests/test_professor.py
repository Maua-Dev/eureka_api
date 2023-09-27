import pytest
from app.models.models import Professor
from app.views import getAllPapers
from tests.MockDB import MockDB
from tests.views_test import addProfessor


@pytest.mark.django_db
def test_my_user():
    MockDB()
    professors = Professor.objects.all()
    assert len(professors) == 2
    
@pytest.mark.django_db
def test_add_professor():
    MockDB()
    professors = Professor.objects.all()
    assert len(professors) == 2
    
    body = {
        'professor_id': 3,
        'name': 'Joao Branco 3',
        'rf': '3BC'
    }
    addProfessor(body)
    
    professors = Professor.objects.all()
    assert len(professors) == 3