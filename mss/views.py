import json

from django.http import HttpResponse, JsonResponse


from mss.models.models import Paper


def index(request):
    return HttpResponse("Hello, world. You're at the mss index.")


def addPaper(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    if request.method == 'POST':
        title = str(body.get('title'))
        shift = str(body.get('shift'))
        professor_id = int(body.get('professor_id'))
        stand_number = int(body.get('stand_number'))

        obj = Paper(title=title, shift=shift, professor_id=professor_id, stand_number=stand_number)

        obj.save()

        return HttpResponse("Paper saved")
    else:
        return HttpResponse("Invalid request method", status=400)

def getAllPapers(request):
    papers = Paper.objects.all()

    return JsonResponse([paper.__dict__() for paper in papers], safe=False)

