import pytest
from app.models.models import Professor
from app.views import getAllPapers
from tests.MockDB import MockDB


@pytest.mark.django_db
def test_my_user():
    MockDB()
    professors = Professor.objects.all()
    assert len(professors) == 2