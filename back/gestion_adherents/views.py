from django.http import Http404
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.reverse import reverse

from .serializers import (
    AdherentsSerializer,
    ArbitreSerializer,
    ArchivesSerializer,
    CatalogueSerializer,
    CategoriesSerializer,
    ContactsSerializer,
    CourrielsSerializer,
    CreneauxSerializer,
    DocumentsSerializer,
    EquipesSerializer,
    EntraineSerializer,
    EntrainementsSerializer,
    PostesSerializer,
    TelephonesSerializer,
    MatchsSerializer,
)
from .models import (
    Adherents,
    Arbitre,
    Archives,
    Catalogue,
    Categories,
    Contacts,
    Courriels,
    Creneaux,
    Documents,
    Equipes,
    Entraine,
    Entrainements,
    Postes,
    Telephones,
    Matchs,
)


@api_view(["GET"])
def apiRoot(request, format=None):
    return Response(
        {
            "adherents": reverse("adherents-list", request=request, format=format),
            "arbitre": reverse("arbitre-list", request=request, format=format),
            "archives": reverse("archives-list", request=request, format=format),
            "catalogue": reverse("catalogue-list", request=request, format=format),
            "categories": reverse("categories-list", request=request, format=format),
            "contacts": reverse("contacts-list", request=request, format=format),
            "courriels": reverse("courriels-list", request=request, format=format),
            "creneaux": reverse("creneaux-list", request=request, format=format),
            "documents": reverse("documents-list", request=request, format=format),
            "entraine": reverse("entraine-list", request=request, format=format),
            "entrainements": reverse(
                "entrainements-list", request=request, format=format
            ),
            "equipes": reverse("equipes-list", request=request, format=format),
            "postes": reverse("postes-list", request=request, format=format),
            "telephones": reverse("telephones-list", request=request, format=format),
            "matchs": reverse("matchs-list", request=request, format=format),
        }
    )


@api_view(["GET", "PUT", "DELETE"])
def adherentsByLicense(request, licenseNumber, format=None):
    """Read, create or delete an Adherent instance (by licenseNumber).

    Args:
        request: The HTTP request.
        licenseNumber: The license number of the object in the database.
    Returns:
        DRF Response.
    """
    try:
        adherent = Adherents.objects.get(no_licence=licenseNumber)  # type: ignore
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = AdherentsSerializer(adherent, context={"request": request})
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = AdherentsSerializer(adherent, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        adherent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AdherentsList(generics.ListCreateAPIView):
    """Read or create Adherents."""

    queryset = Adherents.objects.all()  # type: ignore
    serializer_class = AdherentsSerializer


class AdherentsDetail(generics.RetrieveUpdateDestroyAPIView):
    """Read, update or delete an Adherent instance."""

    queryset = Adherents.objects.all()  # type: ignore
    serializer_class = AdherentsSerializer


class ArbitreList(generics.ListCreateAPIView):
    """Read or create Arbitre."""

    queryset = Arbitre.objects.all()  # type: ignore
    serializer_class = ArbitreSerializer


class ArbitreDetail(generics.RetrieveUpdateDestroyAPIView):
    """Read, update or delete an Arbitre instance."""

    queryset = Arbitre.objects.all()  # type: ignore
    serializer_class = ArbitreSerializer


class ArchivesList(generics.ListCreateAPIView):
    """Read or create Archives."""

    queryset = Archives.objects.all()  # type: ignore
    serializer_class = ArchivesSerializer


class ArchivesDetail(generics.RetrieveUpdateDestroyAPIView):
    """Read, update or delete an Archives instance."""

    queryset = Adherents.objects.all()  # type: ignore
    serializer_class = AdherentsSerializer


class CatalogueList(generics.ListAPIView):
    """Read all Catalogue."""

    queryset = Catalogue.objects.all()  # type: ignore
    serializer_class = CatalogueSerializer


class CatalogueDetail(generics.RetrieveAPIView):
    """Read a Catalogue instance."""

    queryset = Catalogue.objects.all()  # type: ignore
    serializer_class = CatalogueSerializer


class CategoriesList(generics.ListAPIView):
    """Read all Categories."""

    queryset = Categories.objects.all()  # type: ignore
    serializer_class = CategoriesSerializer


class CategoriesDetail(generics.RetrieveAPIView):
    """Read a Categories instance."""

    queryset = Categories.objects.all()  # type: ignore
    serializer_class = CategoriesSerializer


class CreneauxList(generics.ListCreateAPIView):
    """Read or create Creneaux."""

    queryset = Creneaux.objects.all()  # type: ignore
    serializer_class = CreneauxSerializer


class CreneauxDetail(generics.RetrieveAPIView):
    """Read, update or destroy a Creneaux instance."""

    queryset = Creneaux.objects.all()  # type: ignore
    serializer_class = CreneauxSerializer


class DocumentsList(generics.ListCreateAPIView):
    """Read or create Documents."""

    queryset = Documents.objects.all()  # type: ignore
    serializer_class = DocumentsSerializer


class DocumentsDetail(generics.RetrieveAPIView):
    """Read, update or destroy an Documents instance."""

    queryset = Documents.objects.all()  # type: ignore
    serializer_class = DocumentsSerializer


class EquipesList(generics.ListAPIView):
    """Read all Equipes."""

    queryset = Equipes.objects.all()  # type: ignore
    serializer_class = EquipesSerializer


class EquipesDetail(generics.RetrieveAPIView):
    """Read an Equipe instance."""

    queryset = Equipes.objects.all()  # type: ignore
    serializer_class = EquipesSerializer


class EntraineList(generics.ListCreateAPIView):
    """Read or create Entraine."""

    queryset = Entraine.objects.all()  # type: ignore
    serializer_class = EntraineSerializer


class EntraineDetail(generics.RetrieveAPIView):
    """Read, update or destroy an Entraine instance."""

    queryset = Entraine.objects.all()  # type: ignore
    serializer_class = EntraineSerializer


class EntrainementsList(generics.ListCreateAPIView):
    """Read or create Entrainements."""

    queryset = Entrainements.objects.all()  # type: ignore
    serializer_class = EntrainementsSerializer


class EntrainementsDetail(generics.RetrieveAPIView):
    """Read, update or destroy an Entrainements instance."""

    queryset = Entrainements.objects.all()  # type: ignore
    serializer_class = EntrainementsSerializer


@api_view(["GET"])
def entraineDetail(request, adherentId, format=None):
    """Read entraine (by adherentId).

    Args:
        request: The HTTP request.
        adherentId: The adherentId of the object in the database.
    Returns:
        DRF Response (JSON array).
    """
    if request.method == "GET":
        try:
            entraine = Entraine.objects.filter(entraineur=adherentId)  # type: ignore
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EntraineSerializer(
            entraine, context={"request": request}, many=True
        )
        return Response(serializer.data)


class PostesList(generics.ListAPIView):
    """Read all Postes."""

    queryset = Postes.objects.all()  # type: ignore
    serializer_class = PostesSerializer


class PostesDetail(generics.RetrieveAPIView):
    """Read a Postes instance."""

    queryset = Postes.objects.all()  # type: ignore
    serializer_class = PostesSerializer


class CourrielsList(generics.ListCreateAPIView):
    """Read or create Courriels."""

    queryset = Courriels.objects.all()  # type: ignore
    serializer_class = CourrielsSerializer


class CourrielsDetail(generics.RetrieveUpdateDestroyAPIView):
    """Read, update or destroy Courriels instance."""

    queryset = Courriels.objects.all()  # type: ignore
    serializer_class = CourrielsSerializer


@api_view(["GET"])
def courrielsByContactId(request, contactId, format=None):
    """Read courriels (by contactId).

    Args:
        request: The HTTP request.
        contactId: The contactId of the object in the database.
    Returns:
        DRF Response (JSON array).
    """
    if request.method == "GET":
        try:
            courriel = Courriels.objects.filter(contact=contactId)  # type: ignore
            print(len(courriel))
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CourrielsSerializer(
            courriel, context={"request": request}, many=True
        )
        return Response(serializer.data)


class TelephonesList(generics.ListCreateAPIView):
    """Read or create Telephones."""

    queryset = Telephones.objects.all()  # type: ignore
    serializer_class = TelephonesSerializer


class TelephonesDetail(generics.RetrieveUpdateDestroyAPIView):
    """Read, update or delete Telephones instance."""

    queryset = Telephones.objects.all()  # type: ignore
    serializer_class = TelephonesSerializer


@api_view(["GET"])
def telephonesByContactId(request, contactId, format=None):
    """Read a Telephones instance (by contactId).

    Args:
        request: The HTTP request.
        contactId: The contactId of the object in the database.
    Returns:
        DRF Response (JSON array).
    """
    if request.method == "GET":
        try:
            telephone = Telephones.objects.filter(contact=contactId)  # type: ignore
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TelephonesSerializer(telephone, context={"request": request}, many=True)
        return Response(serializer.data)


class ContactsList(generics.ListCreateAPIView):
    """Read or create Contacts"""

    queryset = Contacts.objects.all()  # type: ignore
    serializer_class = ContactsSerializer


class ContactsDetail(generics.RetrieveUpdateDestroyAPIView):
    """Read, update or delete a Contacts instance."""

    queryset = Contacts.objects.all()  # type: ignore
    serializer_class = ContactsSerializer


@api_view(["GET"])
def contactsByAdherentId(request, adherentId, format=None):
    """Read a Contacts instance (by adherentId).

    Args:
        request: The HTTP request.
        adherentId: The adherentId of the object in the database.
    Returns:
        DRF Response.
    """
    if request.method == "GET":
        try:
            contact = Contacts.objects.get(adherent=adherentId)  # type: ignore
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ContactsSerializer(contact, context={"request": request})
        return Response(serializer.data)


class MatchsList(generics.ListCreateAPIView):
    """Read or create Matchs."""

    queryset = Matchs.objects.all()  # type: ignore
    serializer_class = MatchsSerializer


class MatchsDetail(generics.RetrieveUpdateDestroyAPIView):
    """Read, update or delete a Matchs instance."""

    queryset = Matchs.objects.all()  # type: ignore
    serializer_class = MatchsSerializer
