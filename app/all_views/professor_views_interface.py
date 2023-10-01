from abc import abstractmethod
import json

from django.http import HttpResponse, JsonResponse


class ProfessorViewsInterface:
    
    @abstractmethod
    def getAllProfessors(self, request) -> JsonResponse:
        pass
    
    @abstractmethod
    def addProfessor(self, request) -> HttpResponse:
        pass

    @abstractmethod
    def getProfessorById(self, request, id) -> JsonResponse:
        pass
    
    @abstractmethod
    def updateProfessor(self, request) -> HttpResponse:
        pass

