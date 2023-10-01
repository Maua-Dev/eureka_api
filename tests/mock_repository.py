from app.models.models import Professor



class MockDB:
    def __init__(self):
        Professor.objects.create(professor_id=0, name="Joao Branco", rf="ABC")
        Professor.objects.create(professor_id=2, name="Joao Branco 2" , rf="2BC")