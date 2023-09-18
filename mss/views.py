from django.http import HttpResponse, JsonResponse


from mss.models.models import Paper


def index(request):
    return HttpResponse("Hello, world. You're at the mss index.")


def addPaper(request):
    obj = Paper(title="Ronaldo", shift="NIGHT", professor_id=1, stand_number=1)

    obj.save()

    return HttpResponse("Paper saved")


def getAllPapers(request):
    papers = Paper.objects.all()

    return JsonResponse([paper.__dict__() for paper in papers], safe=False)

