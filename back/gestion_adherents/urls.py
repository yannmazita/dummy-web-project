from django.urls import path
from gestion_adherents import views

urlpatterns = [
    path("adherents/", views.adherents),
    path("equipes/", views.equipes),
    path("categories/", views.categories),
]
