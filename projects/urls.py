from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [

    path('projects/', views.project_list, name='project_list'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
]