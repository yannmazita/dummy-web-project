from django.urls import path
from gestion_adherents import views

urlpatterns = [
    path("adherents/", views.adherents),
    path("adherent/<int:id>/", views.adherents),
    path("adherent/no_licence=<int:licenseNumber>/", views.adherentDetail),
    path("equipes/", views.equipes),
    path("categories/", views.categories),
    path("postes/", views.postes),
]
