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
            "categories": reverse("categories-list", request=request, format=format),
            "courriels": reverse("courriels-list", request=request, format=format),
            "entraine": reverse("entraine-list", request=request, format=format),
            "equipes": reverse("equipes-list", request=request, format=format),
            "postes": reverse("postes-list", request=request, format=format),
            "telephones": reverse("telephones-list", request=request, format=format),
        }
    )


@api_view(["GET", "PUT", "DELETE"])
def adherentsLicenseDetail(request, licenseNumber, format=None):
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
    """Read all Equipes."""

    queryset = Adherents.objects.all()  # type: ignore
    serializer_class = AdherentsSerializer


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
            entraine = Entraine.objects.get(entraineur=adherentId)  # type: ignore
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EntraineSerializer(entraine, context={"request": request})
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
            courriel = Courriels.objects.get(contact=contactId)  # type: ignore
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CourrielsSerializer(courriel, context={"request": request})
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
    """Read a Telephones instance (by contactId).

    Args:
        request: The HTTP request.
        contactId: The contactId of the object in the database.
    Returns:
        DRF Response.
    """
    if request.method == "GET":
        try:
            telephone = Telephones.objects.get(contact=contactId)  # type: ignore
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TelephonesSerializer(telephone, context={"request": request})
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
            contact = Contacts.objects.get(adherent=adherentId)  # type: ignore
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ContactsSerializer(contact, context={"request": request})
        return Response(serializer.data)
