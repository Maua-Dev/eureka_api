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

from app import views_first_example
from app.views.professor_views import ProfessorViews


urlpatterns = [
    path('addPaper', views_first_example.addPaper, name='addPaper'),
    path('getAllPapers/', views_first_example.getAllPapers, name='getAllPapers'),
    path('getPaperById/<int:id>', views_first_example.getPaperById, name='getPaperById'),
    path('updatePaper', views_first_example.updatePaper, name='updatePaper'),
    path('getAllProfessors', ProfessorViews.get_all_professors, name='getAllProfessors'),
]
