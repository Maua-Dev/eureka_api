import json

from django.http import HttpResponse, JsonResponse
from app.all_views.professor_views_interface import ProfessorViewsInterface

from app.models.models import Professor

class ProfessorViewsMock(ProfessorViewsInterface):
    def __init__(self):
        self.professors = [
            {
                "professor_id": 1,
                "name": "Professor 1",
                "rf": "123456"
            },
            {
                "professor_id": 2,
                "name": "Professor 2",
                "rf": "654321"
            }
        ]
    
    def getAllProfessors(self, request):
        return JsonResponse([self.professors], safe=False)
    
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
        for professor in self.professors:
            if professor.get("professor_id") == id:
                return JsonResponse(professor, safe=False)
        return JsonResponse({}, safe=False)

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

