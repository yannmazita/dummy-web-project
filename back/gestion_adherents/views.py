from rest_framework.parsers import JSONParser

# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse, JsonResponse
from .serializers import (
    AdherentsSerializer,
    AdherentsPublicSerializer,
    EquipesSerializer,
    CategoriesSerializer,
    PostesSerializer,
)
from .models import Adherents, Equipes, Categories, Postes


@csrf_exempt
def adherents(request, id=None):
    """Creates and Reads adherents.

    Args:
        request: The HTTP request.
        id: The id of the object in the database.
    Returns:
        JSON object or HTTP response.
    """
    if request.method == "GET":
        if id is None:
            if False:
                # Get information that won't break GDPR
                adherents = Adherents.objects.values(  # type: ignore
                    "no_licence", "nom", "prenom", "surclassement", "arbitre", "entraineur"
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
def equipes(request):
    """Read equipes.

    Args:
        request: The HTTP request.
    Returns:
        JSON object or HttpResponse.
    """
    if request.method == "GET":
        try:
            equipes = Equipes.objects.all().values()  # type: ignore
        except:
            return HttpResponse(status=404)
        serializer = EquipesSerializer(equipes, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def categories(request):
    """Read categories.

    Args:
        request: The HTTP request.
    Returns:
        JSON object or HttpResponse.
    """
    if request.method == "GET":
        try:
            categories = Categories.objects.all().values()  # type: ignore
        except:
            return HttpResponse(status=404)
        serializer = CategoriesSerializer(categories, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def postes(request):
    """Read postes.

    Args:
        request: The HTTP request.
    Returns:
        JSON object or HttpResponse.
    """
    if request.method == "GET":
        try:
            postes = Postes.objects.all().values()  # type: ignore
        except:
            return HttpResponse(status=404)
        serializer = PostesSerializer(postes, many=True)
        return JsonResponse(serializer.data, safe=False)
