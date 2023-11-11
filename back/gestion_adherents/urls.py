from django.urls import path
from gestion_adherents import views

urlpatterns = [
    path("adherents/", views.adherents),
    path("adherent/<int:id>/", views.adherents),
    path("adherent/no_licence=<int:licenseNumber>/", views.adherentDetail),
    path("equipes/", views.equipes),
    path("equipe/<int:id>", views.equipes),
    path("entrainees/", views.entraine),
    path("entraine/<int:id>", views.entraine),
    path("entraine/adherent_id=<int:adherentId>", views.entraineDetail),
    path("categories/", views.categories),
    path("categorie/<int:id>", views.categories),
    path("postes/", views.postes),
    path("poste/<int:id>", views.postes),
]
