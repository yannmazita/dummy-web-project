from rest_framework.parsers import JSONParser

# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse
from .serializers import (
    AdherentsSerializer,
    AdherentsPublicSerializer,
    EquipesSerializer,
    CategoriesSerializer,
)
from .models import Adherents, Equipes, Categories, Postes


@csrf_exempt
def adherents(request):
    """Create and Read adherents."""
    if request.method == "GET":
        # Get information that won't break GDPR
        adherents = Adherents.objects.values(  # type: ignore
            "no_licence", "nom", "prenom", "surclassement", "arbitre", "entraineur"
        )
        serializer = AdherentsPublicSerializer(adherents, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)

        print(f"data={data}")

        # ! Django names indexing primary keys "id" by default
        id_categorie = Categories.objects.filter(  # type: ignore
            categorie=f"{data['categorie']}"
        ).values("id")
        id_poste = Postes.objects.filter(  # type: ignore
            designation=f"{data['dirigeant']}"
        ).values("id")

        print(f"\nid_categorie={id_categorie}")
        print(f"\nid_poste={id_poste}")

        data["id_categorie"] = id_categorie
        data["id_poste"] = id_poste

        print(f"\ndata['id_categorie']={id_categorie}")
        print(f"\ndata['id_poste']={id_poste}")

        serializer = AdherentsSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        print(f"\n{serializer.errors}")
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def equipes(request):
    """Read equipes."""
    if request.method == "GET":
        equipes = Equipes.objects.all().values()  # type: ignore
        serializer = EquipesSerializer(equipes, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def categories(request):
    """Read categories."""
    if request.method == "GET":
        categories = Categories.objects.all().values()  # type: ignore
        serializer = CategoriesSerializer(categories, many=True)
        return JsonResponse(serializer.data, safe=False)
