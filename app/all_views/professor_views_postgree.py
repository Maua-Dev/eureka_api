import json

from django.http import HttpResponse, JsonResponse
from app.all_views.professor_views_interface import ProfessorViewsInterface

from app.models.models import Professor

class ProfessorViewsPostgree(ProfessorViewsInterface):
    
    def __init__(self):
        pass
    
    def getAllProfessors(self, request):
        professors = Professor.objects.all()
        return JsonResponse([professor.to_dict() for professor in professors], safe=False)
    
    def addProfessor(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        if request.method == 'POST':
            name = str(body.get('name'))
            rf = str(body.get('rf'))
            Professor.objects.create(name=name, rf=rf)

            return HttpResponse("Professor saved")
        else:
            return HttpResponse("Invalid request method", status=400)

    def getProfessorById(self, request, id):
        professor = Professor.objects.get(professor_id=id)

        return JsonResponse(professor.to_dict(), safe=False)

    def updateProfessor(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        if request.method == 'PUT':
            id = int(body.get('professor_id'))
            name = str(body.get('name'))
            rf = str(body.get('rf'))

            professor = Professor.objects.get(professor_id=id)
            professor.name = name
            professor.rf = rf
            professor.save()

            return HttpResponse("Professor updated")
        else:
            return HttpResponse("Invalid request method", status=400)

