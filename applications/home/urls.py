from django.urls import path

from applications.home import views

urlpatterns = [
    path('index/', views.indexView.as_view()),
    path('lista/', views.pruebaListaView.as_view()),
]