from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
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
    path("courriels/", views.courriels),
    path("courriel/<int:id>", views.courriels),
    path("courriel/contact_id=<int:contactId>", views.courrielsDetail),
    path("telephones/", views.telephones),
    path("telephone/<int:id>", views.telephones),
    path("telephone/contact_id=<int:contactId>", views.telephonesDetail),
    path("contacts/", views.contacts),
    path("contact/<int:id>", views.contacts),
    path("contact/adherent_id=<int:adherentId>", views.contactsDetail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
