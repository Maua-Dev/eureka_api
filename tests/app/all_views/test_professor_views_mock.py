import json
import pytest
from app.all_views.professor_views_mock import ProfessorViewsMock
from app.models.models import Professor
from app.views import getAllPapers
from tests.mock_repository import MockDB
from tests.views_test import addProfessor

def request_item_to_dict(request):
    return json.loads(str(request._container[0])[2:-1])

def request_list_to_dict(request):
    return json.loads(str(request._container[0])[3:-2])

@pytest.mark.django_db
def test_get_all_professors():
    mock = ProfessorViewsMock()
    request = mock.getAllProfessors({})
    assert len(request_list_to_dict(request)) == 2
    
@pytest.mark.django_db
def test_get_professor_by_id():
    mock = ProfessorViewsMock()
    request = mock.getProfessorById({}, 1)
    assert mock.professors[0] == request_item_to_dict(request)
    
# @pytest.mark.django_db
# def test_get_professor_by_id():
#     mock = ProfessorViewsMock()
#     request = mock.getProfessorById({}, 1)
#     print(request_item_to_dict(request))
#     assert mock.professors[0] == request_item_to_dict(request)