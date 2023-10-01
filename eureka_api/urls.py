"""
URL configuration for eureka_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from app import views
from app.all_views import professor_views_postgree


professor_views = professor_views_postgree.ProfessorViewsPostgree()

urlpatterns = [
    path('addPaper', views.addPaper, name='addPaper'),
    path('getAllPapers/', views.getAllPapers, name='getAllPapers'),
    path('getPaperById/<int:id>', views.getPaperById, name='getPaperById'),
    path('updatePaper', views.updatePaper, name='updatePaper'),
    
    
    path('getAllProfessors/', professor_views.getAllProfessors, name='getAllProfessors'),
    path('addProfessor', professor_views.addProfessor, name='addProfessor'),
    path('getProfessorById/<int:id>', professor_views.getProfessorById, name='getProfessorById'),
    path('updateProfessor', professor_views.updateProfessor, name='updateProfessor'),

    
]
