import factory 

from django.contrib.auth.models import User
from app.models.models import Professor  


class ProfessorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Professor

    professor_id = '0'
    name = 'Vanderlei'
    rf = 'SDC'