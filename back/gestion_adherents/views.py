from rest_framework.parsers import JSONParser

# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse
from .serializers import (
    AdherentsSerializer,
    AdherentsPublicSerializer,
    EquipesSerializer,
)
from .models import Adherents, Equipes


@csrf_exempt
def adherents(request):
    """Create and Read adherents"""
    if request.method == "GET":
        # Get information that won't break GDPR
        adherents = Adherents.objects.values_list(  # type: ignore
            "no_licence", "nom", "prenom", "surclassement", "arbitre", "entraineur"
        )
        serializer = AdherentsPublicSerializer(adherents, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = AdherentsSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def equipes(request):
    """Read equipes"""
    if request.method == "GET":
        equipes = Equipes.objects.all()  # type: ignore
        serializer = EquipesSerializer(equipes, many=True)
        return JsonResponse(serializer.data, safe=False)
