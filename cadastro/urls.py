from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/caminhao', views.CaminhaoListCreate.as_view()),
]