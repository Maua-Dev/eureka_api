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

from app.views.task_views import TaskViews
from app.views.project_views import ProjectViews

urlpatterns = [
    path('get_all_tasks', TaskViews.get_all_tasks, name='get_all_tasks'),
    path('create_project', ProjectViews.create_project, name='create_project'),
    path('update_project', ProjectViews.update_project, name='update_project'),
    path('get_project', ProjectViews.get_project, name='get_project'),
]
