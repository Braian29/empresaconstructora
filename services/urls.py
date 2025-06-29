from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('', views.service_list, name='service_list'),
    path('<slug:slug>/', views.ServiceDetailView.as_view(), name='service_detail'),
]