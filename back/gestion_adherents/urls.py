from django.urls import path
from gestion_adherents import views

urlpatterns = [
    path("adherents.json", views.adherents),
    path("equipes.json", views.equipes),
]
