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
    AdherentsPublicSerializer,
    CategoriesSerializer,
    ContactsSerializer,
    CourrielsSerializer,
    EquipesSerializer,
    EntraineSerializer,
    PostesSerializer,
    TelephonesSerializer,
)
from .models import (
    Adherents,
    Categories,
    Contacts,
    Courriels,
    Equipes,
    Entraine,
    Postes,
    Telephones,
)


@api_view(["GET"])
def apiRoot(request, format=None):
    return Response(
        {
            "adherents": reverse("adherents-list", request=request, format=format),
            "equipes": reverse("equipes-list", request=request, format=format),
        }
    )


class AdherentsList(APIView):
    """Read all Adherents or create a new Adherent."""

    def get(self, request, format=None):
        adherents = Adherents.objects.all()  # type: ignore
        serializer = AdherentsSerializer(adherents, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        adherentSerializer = AdherentsSerializer(data=data)
        if adherentSerializer.is_valid():
            adherentSerializer.save()
            return Response(adherentSerializer.data, status=status.HTTP_201_CREATED)


class AdherentsDetail(generics.RetrieveUpdateDestroyAPIView):
    """Read, update or delete an Adherent instance."""

    queryset = Adherents.objects.all()  # type: ignore
    serializer_class = AdherentsSerializer


class EquipesList(generics.ListAPIView):
    """Read all Equipes."""

    queryset = Equipes.objects.all()  # type: ignore
    serializer_class = EquipesSerializer


class EquipesDetail(generics.RetrieveAPIView):
    """Read an Equipe instance."""

    queryset = Equipes.objects.all()  # type: ignore
    serializer_class = EquipesSerializer


class EntraineList(generics.ListAPIView):
    """Read all Entraine."""

    queryset = Entraine.objects.all()  # type: ignore
    serializer_class = EntraineSerializer


class EntraineDetail(generics.RetrieveAPIView):
    """Read an Entraine instance."""

    queryset = Entraine.objects.all()  # type: ignore
    serializer_class = EntraineSerializer


@api_view(["GET"])
def entraineDetail(request, adherentId, format=None):
    """Read entraine (by adherentId).

    Args:
        request: The HTTP request.
        adherentId: The adherentId of the object in the database.
    Returns:
        DRF Response.
    """
    if request.method == "GET":
        try:
            entraine = Entraine.objects.get(adherent_id=adherentId)  # type: ignore
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EntraineSerializer(entraine)
        return Response(serializer.data)


class CategoriesList(generics.ListAPIView):
    """Read all Categories."""

    queryset = Categories.objects.all()  # type: ignore
    serializer_class = CategoriesSerializer


class CategoriesDetail(generics.RetrieveAPIView):
    """Read a Categories instance."""

    queryset = Categories.objects.all()  # type: ignore
    serializer_class = CategoriesSerializer


class PostesList(generics.ListAPIView):
    """Read all Postes."""

    queryset = Postes.objects.all()  # type: ignore
    serializer_class = PostesSerializer


class PostesDetail(generics.RetrieveAPIView):
    """Read a Postes instance."""

    queryset = Postes.objects.all()  # type: ignore
    serializer_class = PostesSerializer


class CourrielsList(generics.ListAPIView):
    """Read all Courriels."""

    queryset = Courriels.objects.all()  # type: ignore
    serializer_class = CourrielsSerializer


class CourrielsDetail(generics.RetrieveAPIView):
    """Read a Courriels instance."""

    queryset = Courriels.objects.all()  # type: ignore
    serializer_class = CourrielsSerializer


@api_view(["GET"])
def courrielsDetail(request, contactId, format=None):
    """Read courriels (by contactId).

    Args:
        request: The HTTP request.
        contactId: The contactId of the object in the database.
    Returns:
        DRF Response.
    """
    if request.method == "GET":
        try:
            courriel = Courriels.objects.get(contact_id=contactId)  # type: ignore
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CourrielsSerializer(courriel)
        return Response(serializer.data)


class TelephonesList(generics.ListAPIView):
    """Read all Telephones."""

    queryset = Telephones.objects.all()  # type: ignore
    serializer_class = TelephonesSerializer


class TelephonesDetail(generics.RetrieveAPIView):
    """Read a Telephones instance."""

    queryset = Telephones.objects.all()  # type: ignore
    serializer_class = TelephonesSerializer


@api_view(["GET"])
def telephonesDetail(request, contactId, format=None):
    """Read contacts (by contactId).

    Args:
        request: The HTTP request.
        contactId: The contactId of the object in the database.
    Returns:
        DRF Response.
    """
    if request.method == "GET":
        try:
            contact = Contacts.objects.get(contact_id=contactId)  # type: ignore
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TelephonesSerializer(contact)
        return Response(serializer.data)


class ContactsList(generics.ListAPIView):
    """Read all Contacts."""

    queryset = Contacts.objects.all()  # type: ignore
    serializer_class = ContactsSerializer


class ContactsDetail(generics.RetrieveAPIView):
    """Read a Contacts instance."""

    queryset = Contacts.objects.all()  # type: ignore
    serializer_class = ContactsSerializer


@api_view(["GET"])
def contactsDetail(request, adherentId, format=None):
    """Read contacts (by adherentId).

    Args:
        request: The HTTP request.
        adherentId: The adherentId of the object in the database.
    Returns:
        DRF Response.
    """
    if request.method == "GET":
        try:
            contact = Contacts.objects.get(adherent_id=adherentId)  # type: ignore
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ContactsSerializer(contact)
        return Response(serializer.data)
