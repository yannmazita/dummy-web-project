from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from gestion_adherents import views

urlpatterns = [
    path("", views.apiRoot),
    path("adherents/", views.AdherentsList.as_view(), name="adherents-list"),
    path(
        "adherents/<int:pk>/", views.AdherentsDetail.as_view(), name="adherents-detail"
    ),
    # path("adherents/no_licence=<int:licenseNumber>/", views.AdherentsDetail({"get": "getByLicenseNumber"})),
    path("equipes/", views.EquipesList.as_view(), name="equipes-list"),
    path("equipes/<int:pk>", views.EquipesDetail.as_view(), name="equipes-detail"),
    path("entraine/", views.EntraineList.as_view(), name="entraine-list"),
    path("entraine/<int:pk>", views.EntraineDetail.as_view(), name="entraine-detail"),
    path("entraine/adherent_id=<int:adherentId>", views.entraineDetail),
    path("categories/", views.CategoriesList.as_view(), name="categories-list"),
    path(
        "categories/<int:pk>", views.CategoriesDetail.as_view(), name="categories-detail"
    ),
    path("postes/", views.PostesList.as_view(), name="postes-list"),
    path("postes/<int:pk>", views.PostesDetail.as_view(), name="postes-detail"),
    path("courriels/", views.CourrielsList.as_view(), name="courriels-list"),
    path("courriels/<int:pk>", views.CourrielsDetail.as_view(), name="courriels-detail"),
    path("courriels/contact_id=<int:contactId>", views.courrielsDetail),
    path("telephones/", views.TelephonesList.as_view(), name="telephones-list"),
    path(
        "telephones/<int:id>", views.TelephonesDetail.as_view(), name="telephones-detail"
    ),
    path("telephones/contact_id=<int:contactId>", views.telephonesDetail),
    path("contacts/", views.ContactsList.as_view(), name="contacts-list"),
    path("contacts/<int:pk>", views.ContactsDetail.as_view(), name="contact-detail"),
    path("contacts/adherent_id=<int:adherentId>", views.contactsDetail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
