from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from gestion_adherents import views

urlpatterns = [
    path("", views.apiRoot),
    path("adherents/", views.AdherentsList.as_view(), name="adherents-list"),
    path(
        "adherents/<int:pk>/", views.AdherentsDetail.as_view(), name="adherents-detail"
    ),
    path("adherents/no_licence=<int:licenceNumber>/", views.adherentsByLicense),
    path("arbitre/", views.ArbitreList.as_view(), name="arbitre-list"),
    path("arbitre/<int:pk>", views.ArbitreDetail.as_view(), name="arbitre-detail"),
    path("archives/", views.ArchivesList.as_view(), name="archives-list"),
    path("archives/<int:pk>", views.ArchivesDetail.as_view(), name="archives-detail"),
    path("catalogue/", views.CatalogueList.as_view(), name="catalogue-list"),
    path(
        "catalogue/<int:pk>", views.CatalogueDetail.as_view(), name="catalogue-detail"
    ),
    path("categories/", views.CategoriesList.as_view(), name="categories-list"),
    path(
        "categories/<int:pk>",
        views.CategoriesDetail.as_view(),
        name="categories-detail",
    ),
    path("contacts/", views.ContactsList.as_view(), name="contacts-list"),
    path("contacts/<int:pk>", views.ContactsDetail.as_view(), name="contacts-detail"),
    path("contacts/adherent_id=<int:adherentId>", views.contactsByAdherentId),
    path("courriels/", views.CourrielsList.as_view(), name="courriels-list"),
    path(
        "courriels/<int:pk>", views.CourrielsDetail.as_view(), name="courriels-detail"
    ),
    path("courriels/contact_id=<int:contactId>", views.courrielsByContactId),
    path("creneaux/", views.CreneauxList.as_view(), name="creneaux-list"),
    path("creneaux/<int:pk>", views.CreneauxDetail.as_view(), name="creneaux-detail"),
    path("documents/", views.DocumentsList.as_view(), name="documents-list"),
    path("documents/<int:pk>", views.DocumentsDetail.as_view(), name="documents-detail"),
    path("entraine/", views.EntraineList.as_view(), name="entraine-list"),
    path("entraine/<int:pk>", views.EntraineDetail.as_view(), name="entraine-detail"),
    path("entraine/adherent_id=<int:adherentId>", views.entraineDetail),
    path("entrainements/", views.EntrainementsList.as_view(), name="entrainements-list"),
    path("entrainements/<int:pk>", views.EntraineDetail.as_view(), name="entrainements-detail"),
    path("equipes/", views.EquipesList.as_view(), name="equipes-list"),
    path("equipes/<int:pk>", views.EquipesDetail.as_view(), name="equipes-detail"),
    path("postes/", views.PostesList.as_view(), name="postes-list"),
    path("postes/<int:pk>", views.PostesDetail.as_view(), name="postes-detail"),
    path("telephones/", views.TelephonesList.as_view(), name="telephones-list"),
    path(
        "telephones/<int:id>",
        views.TelephonesDetail.as_view(),
        name="telephones-detail",
    ),
    path("telephones/contact_id=<int:contactId>", views.telephonesDetail),
    path("matchs/", views.MatchsList.as_view(), name="matchs-list"),
    path("matchs/<int:pk>", views.MatchsDetail.as_view(), name="matchs-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
