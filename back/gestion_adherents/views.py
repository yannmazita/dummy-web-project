# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse, JsonResponse
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


@csrf_exempt
def adherents(request, id=None):
    """Creates and Reads adherents.

    Args:
        request: The HTTP request.
        id: The id (primary key) of the object in the database.
    Returns:
        JSON object or HTTP response.
    """
    if request.method == "GET":
        if id is None:
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
                return JsonResponse(serializer.data, safe=False)
            if True:
                # Get everything
                adherents = Adherents.objects.all().values()  # type: ignore
                serializer = AdherentsSerializer(adherents, many=True)
                return JsonResponse(serializer.data, safe=False)
        else:
            try:
                adherent = Adherents.objects.get(pk=id)  # type: ignore
            except:
                return HttpResponse(status=404)
            serializer = AdherentsSerializer(adherent)
            return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        pass


@csrf_exempt
def adherentDetail(request, licenseNumber):
    """Reads adherents (by licenseNumber).

    Args:
        request: The HTTP request.
        licenseNumber: The licenseNumber of the object in the database.
    Returns:
        JSON object or HTTP response.
    """
    if request.method == "GET":
        try:
            adherent = Adherents.objects.get(no_licence=licenseNumber)  # type: ignore
        except:
            return HttpResponse(status=404)
        serializer = AdherentsSerializer(adherent)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def equipes(request, id=None):
    """Read equipes.

    Args:
        request: The HTTP request.
        id: The id (primary key) of the object in the database.
    Returns:
        JSON object or HttpResponse.
    """
    if request.method == "GET":
        if id is None:
            try:
                equipes = Equipes.objects.all().values()  # type: ignore
            except:
                return HttpResponse(status=404)
            serializer = EquipesSerializer(equipes, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            try:
                equipe = Equipes.objects.get(id=id)  # type: ignore
            except:
                return HttpResponse(status=404)
            serializer = EquipesSerializer(equipe)
            return JsonResponse(serializer, safe=False)


@csrf_exempt
def entraine(request, id=None):
    """Read entraine.

    Args:
        request: The HTTP request.
        id: The id (primary key) of the object in the database.
    Returns:
        JSON object or HttpResponse.
    """
    if request.method == "GET":
        if id is None:
            try:
                entraines = Entraine.objects.all().values()  # type: ignore
            except:
                return HttpResponse(status=404)
            serializer = EntraineSerializer(entraines, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            try:
                entraine = Equipes.objects.get(id=id)  # type: ignore
            except:
                return HttpResponse(status=404)
            serializer = EquipesSerializer(entraine)
            return JsonResponse(serializer, safe=False)


@csrf_exempt
def entraineDetail(request, adherentId):
    """Read entraine (by adherentId).

    Args:
        request: The HTTP request.
        adherentId: The adherentId of the object in the database.
    Returns:
        JSON object or HTTP response.
    """
    if request.method == "GET":
        try:
            entraine = Entraine.objects.get(adherent_id=adherentId)  # type: ignore
        except:
            return HttpResponse(status=404)
        serializer = EntraineSerializer(entraine)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def categories(request, id=None):
    """Read categories.

    Args:
        request: The HTTP request.
        id: The id (primary key) of the object in the database.
    Returns:
        JSON object or HttpResponse.
    """
    if request.method == "GET":
        if id is None:
            try:
                categories = Categories.objects.all().values()  # type: ignore
            except:
                return HttpResponse(status=404)
            serializer = CategoriesSerializer(categories, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            try:
                categorie = Categories.objects.get(id=id)  # type: ignore
            except:
                return HttpResponse(status=404)
            serializer = CategoriesSerializer(categorie)
            return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def postes(request, id=None):
    """Read postes.

    Args:
        request: The HTTP request.
        id: The id (primary key) of the object in the database.
    Returns:
        JSON object or HttpResponse.
    """
    if request.method == "GET":
        if id is None:
            try:
                postes = Postes.objects.all().values()  # type: ignore
            except:
                return HttpResponse(status=404)
            serializer = PostesSerializer(postes, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            try:
                poste = Postes.objects.get(id=id)  # type: ignore
            except:
                return HttpResponse(status=404)
            serializer = PostesSerializer(poste)
            return JsonResponse(serializer, safe=False)


@csrf_exempt
def courriels(request, id=None):
    """Read courriels.

    Args:
        request: The HTTP request.
        id: The id (primary key) of the object in the database.
    Returns:
        JSON object or HttpResponse.
    """
    if request.method == "GET":
        if id is None:
            try:
                courriels = Courriels.objects.all().values()  # type: ignore
            except:
                return HttpResponse(status=404)
            serializer = CourrielsSerializer(courriels, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            try:
                courriel = Courriels.objects.get(id=id)  # type: ignore
            except:
                return HttpResponse(status=404)
            serializer = CourrielsSerializer(courriel)
            return JsonResponse(serializer, safe=False)


@csrf_exempt
def courrielsDetail(request, contactId):
    """Read courriels (by contactId).

    Args:
        request: The HTTP request.
        contactId: The contactId of the object in the database.
    Returns:
        JSON object or HTTP response.
    """
    if request.method == "GET":
        try:
            courriel = Courriels.objects.get(contact_id=contactId)  # type: ignore
        except:
            return HttpResponse(status=404)
        serializer = CourrielsSerializer(courriel)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def telephones(request, id=None):
    """Read telephones.

    Args:
        request: The HTTP request.
        id: The id (primary key) of the object in the database.
    Returns:
        JSON object or HttpResponse.
    """
    if request.method == "GET":
        if id is None:
            try:
                telephones = Telephones.objects.all().values()  # type: ignore
            except:
                return HttpResponse(status=404)
            serializer = TelephonesSerializer(telephones, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            try:
                telephone = Telephones.objects.get(id=id)  # type: ignore
            except:
                return HttpResponse(status=404)
            serializer = TelephonesSerializer(telephone)
            return JsonResponse(serializer, safe=False)


@csrf_exempt
def telephonesDetail(request, contactId):
    """Read contacts (by contactId).

    Args:
        request: The HTTP request.
        contactId: The contactId of the object in the database.
    Returns:
        JSON object or HTTP response.
    """
    if request.method == "GET":
        try:
            contact = Contacts.objects.get(contact_id=contactId)  # type: ignore
        except:
            return HttpResponse(status=404)
        serializer = TelephonesSerializer(contact)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def contacts(request, id=None):
    """Read contacts.

    Args:
        request: The HTTP request.
        id: The id (primary key) of the object in the database.
    Returns:
        JSON object or HttpResponse.
    """
    if request.method == "GET":
        if id is None:
            try:
                contacts = Contacts.objects.all().values()  # type: ignore
            except:
                return HttpResponse(status=404)
            serializer = ContactsSerializer(contacts, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            try:
                contact = Contacts.objects.get(id=id)  # type: ignore
            except:
                return HttpResponse(status=404)
            serializer = ContactsSerializer(contact)
            return JsonResponse(serializer, safe=False)


@csrf_exempt
def contactsDetail(request, adherentId):
    """Read contacts (by adherentId).

    Args:
        request: The HTTP request.
        adherentId: The adherentId of the object in the database.
    Returns:
        JSON object or HTTP response.
    """
    if request.method == "GET":
        try:
            contact = Contacts.objects.get(adherent_id=adherentId)  # type: ignore
        except:
            return HttpResponse(status=404)
        serializer = ContactsSerializer(contact)
        return JsonResponse(serializer.data, safe=False)
