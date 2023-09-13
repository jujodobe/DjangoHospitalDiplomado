from django.contrib import admin
from django.urls import path
from applications.pacientes import views

urlpatterns = [
    path('index/', views.PacientesListView.as_view()),
    path('api/listado/', views.PacientesListApiView.as_view()),
    path('api/registro', views.PacientesRegisterApiView.as_view())
]