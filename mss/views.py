from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse

from mss.models.models import Paper


def index(request):
    return HttpResponse("Hello, world. You're at the mss index.")

def addPaper(request):

    obj = Paper(title="Ronaldo", shift="NIGHT", professor_id=1, stand_number=1)

    obj.save()

    return HttpResponse("Paper saved")
