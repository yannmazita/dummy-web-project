from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from gestion_adherents import views

urlpatterns = [
    path("", views.apiRoot),
    path("adherents/", views.AdherentsList.as_view(), name="adherents-list"),
    path(
        "adherent/<int:id>/", views.AdherentsDetail.as_view(), name="adherents-detail"
    ),
    # path("adherent/no_licence=<int:licenseNumber>/", views.AdherentsDetail({"get": "getByLicenseNumber"})),
    path("equipes/", views.EquipesList.as_view(), name="equipes-list"),
    path("equipe/<int:pk>", views.EquipesDetail.as_view(), name="equipes-detail"),
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
