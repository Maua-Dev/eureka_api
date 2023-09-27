import json

from django.http import HttpResponse

from app.models.models import Professor


def addProfessor(request):
    body = request

    professor_id = str(body.get('professor_id'))
    name = str(body.get('name'))
    rf = str(body.get('rf'))

    Professor.objects.create(professor_id=professor_id, name=name, rf=rf)
    return HttpResponse("Paper saved")