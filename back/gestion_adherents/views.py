from django.http import Http404
from rest_framework import status
from rest_framework import generics
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
        if False:
            # Get information that won't break GDPR
            adherents = Adherents.objects.values(  # type: ignore
                "no_licence",
                "nom",
                "prenom",
                "surclassement",
                "arbitre",
                "entraineur",
            )
            serializer = AdherentsPublicSerializer(adherents, many=True)
            return Response(serializer.data)
        if True:
            # Get everything
            adherents = Adherents.objects.all().values()  # type: ignore
            serializer = AdherentsSerializer(adherents, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        pass


class AdherentsDetail(APIView):
    """Read, update or delete a snippet instance."""

    def getObjectByID(self, id):
        try:
            return Adherents.objects.get(id=id)  # type: ignore
        except:
            raise Http404

    def getObjectByLicenseNumber(self, licenseNumber):
        try:
            return Adherents.objects.get(no_licence=licenseNumber)  # type: ignore
        except:
            raise Http404

    def getByID(self, request, id, format=None):
        adherent = self.getObjectByID(id)
        serializer = AdherentsSerializer(adherent)
        return Response(serializer.data)

    def getByLicenseNumber(self, request, licenseNumber, format=None):
        adherent = self.getObjectByLicenseNumber(licenseNumber)
        serializer = AdherentsSerializer(adherent)
        return Response(serializer.data)

    def putByID(self, request, id, format=None):
        adherent = self.getObjectByID(id)
        print(request.data)


class EquipesList(generics.ListAPIView):
    queryset = Equipes.objects.all()  # type: ignore
    serializer_class = EquipesSerializer


class EquipesDetail(generics.RetrieveAPIView):
    queryset = Equipes.objects.all()  # type: ignore
    serializer_class = EquipesSerializer


@api_view(["GET"])
def equipes(request, id=None, format=None):
    """Read equipes.

    Args:
        request: The HTTP request.
        id: The id (primary key) of the object in the database.
    Returns:
        DRF Response.
    """
    if request.method == "GET":
        if id is None:
            try:
                equipes = Equipes.objects.all().values()  # type: ignore
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = EquipesSerializer(equipes, many=True)
            return Response(serializer.data)
        else:
            try:
                equipe = Equipes.objects.get(id=id)  # type: ignore
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = EquipesSerializer(equipe)
            return Response(serializer.data)


@api_view(["GET"])
def entraine(request, id=None, format=None):
    """Read entraine.

    Args:
        request: The HTTP request.
        id: The id (primary key) of the object in the database.
    Returns:
        DRF Response.
    """
    if request.method == "GET":
        if id is None:
            try:
                entraines = Entraine.objects.all().values()  # type: ignore
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = EntraineSerializer(entraines, many=True)
            return Response(serializer.data)
        else:
            try:
                entraine = Equipes.objects.get(id=id)  # type: ignore
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = EquipesSerializer(entraine)
            return Response(serializer.data)


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


@api_view(["GET"])
def categories(request, id=None, format=None):
    """Read categories.

    Args:
        request: The HTTP request.
        id: The id (primary key) of the object in the database.
    Returns:
        DRF Response.
    """
    if request.method == "GET":
        if id is None:
            try:
                categories = Categories.objects.all().values()  # type: ignore
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = CategoriesSerializer(categories, many=True)
            return Response(serializer.data)
        else:
            try:
                categorie = Categories.objects.get(id=id)  # type: ignore
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = CategoriesSerializer(categorie)
            return Response(serializer.data)


@api_view(["GET"])
def postes(request, id=None, format=None):
    """Read postes.

    Args:
        request: The HTTP request.
        id: The id (primary key) of the object in the database.
    Returns:
        DRF Response.
    """
    if request.method == "GET":
        if id is None:
            try:
                postes = Postes.objects.all().values()  # type: ignore
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = PostesSerializer(postes, many=True)
            return Response(serializer.data)
        else:
            try:
                poste = Postes.objects.get(id=id)  # type: ignore
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = PostesSerializer(poste)
            return Response(serializer.data)


@api_view(["GET"])
def courriels(request, id=None, format=None):
    """Read courriels.

    Args:
        request: The HTTP request.
        id: The id (primary key) of the object in the database.
    Returns:
        DRF Response.
    """
    if request.method == "GET":
        if id is None:
            try:
                courriels = Courriels.objects.all().values()  # type: ignore
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = CourrielsSerializer(courriels, many=True)
            return Response(serializer.data)
        else:
            try:
                courriel = Courriels.objects.get(id=id)  # type: ignore
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = CourrielsSerializer(courriel)
            return Response(serializer.data)


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


@api_view(["GET"])
def telephones(request, id=None, format=None):
    """Read telephones.

    Args:
        request: The HTTP request.
        id: The id (primary key) of the object in the database.
    Returns:
        DRF Response.
    """
    if request.method == "GET":
        if id is None:
            try:
                telephones = Telephones.objects.all().values()  # type: ignore
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = TelephonesSerializer(telephones, many=True)
            return Response(serializer.data)
        else:
            try:
                telephone = Telephones.objects.get(id=id)  # type: ignore
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = TelephonesSerializer(telephone)
            return Response(serializer.data)


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


@api_view(["GET"])
def contacts(request, id=None, format=None):
    """Read contacts.

    Args:
        request: The HTTP request.
        id: The id (primary key) of the object in the database.
    Returns:
        DRF Response.
    """
    if request.method == "GET":
        if id is None:
            try:
                contacts = Contacts.objects.all().values()  # type: ignore
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = ContactsSerializer(contacts, many=True)
            return Response(serializer.data)
        else:
            try:
                contact = Contacts.objects.get(id=id)  # type: ignore
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = ContactsSerializer(contact)
            return Response(serializer.data)


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
