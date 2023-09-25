import factory 

from app.models.models import Professor  


class ProfessorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Professor

    professor_id = '0'
    name = 'Vanderlei'
    rf = 'SDC'