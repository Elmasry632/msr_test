from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.projects_details, name='projects_details'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'), 
]
