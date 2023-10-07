import json

from django.http import HttpResponse, JsonResponse

from .models.models import Paper



def addPaper(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    if request.method == 'POST':
        title = str(body.get('title'))
        shift = str(body.get('shift'))
        professor_id = int(body.get('professor_id'))
        stand_number = int(body.get('stand_number'))

        Paper.objects.create(title=title, shift=shift, professor_id=professor_id, stand_number=stand_number)

        return HttpResponse("Paper saved")
    else:
        return HttpResponse("Invalid request method", status=400)

def getAllPapers(request):
    papers = Paper.objects.all()

    return JsonResponse([paper.to_dict() for paper in papers], safe=False, status=200)

def getPaperById(request, id):
    paper = Paper.objects.get(assigment_id=id)

    return JsonResponse(paper.to_dict(), safe=False)

def updatePaper(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    if request.method == 'PUT':
        id = int(body.get('assigment_id'))
        title = str(body.get('title'))
        shift = str(body.get('shift'))
        professor_id = int(body.get('professor_id'))
        stand_number = int(body.get('stand_number'))

        paper = Paper.objects.get(assigment_id=id)
        paper.title = title
        paper.shift = shift
        paper.professor_id = professor_id
        paper.stand_number = stand_number
        paper.save()

        return HttpResponse("Paper updated")
    else:
        return HttpResponse("Invalid request method", status=400)

