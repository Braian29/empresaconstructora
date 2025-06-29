from django.urls import path
from . import views
from projects import views as project_views

app_name = 'core'

urlpatterns = [
    path('', project_views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
]