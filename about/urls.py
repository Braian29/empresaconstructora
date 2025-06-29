from django.urls import path
from . import views

app_name = 'about'

urlpatterns = [
    path('', views.AboutUsView.as_view(), name='about'),
]