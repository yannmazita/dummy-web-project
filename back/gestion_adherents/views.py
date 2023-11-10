# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse, JsonResponse
import json
from .serializers import (
    AdherentsSerializer,
    AdherentsPublicSerializer,
    EquipesSerializer,
    CategoriesSerializer,
    PostesSerializer,
)
from .models import Adherents, Equipes, Categories, Postes, Courriels, Telephones


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
        data = json.loads(request.body)
        print("==================")
        print(data.get("arbitre", False)) # OK
        print(data.get("categorie")) # OK
        print(data.get("date_naissance")) # OK
        print(data.get("dirigeant")) # OK
        print(data.get("email")) # bad specs
        print(data.get("equipe")) # TODO
        print(data.get("genre")) # OK
        print(data.get("habilitation")) # OK
        print(data.get("no_licence")) # OK
        print(data.get("nom")) # OK
        print(data.get("prenom")) # OK
        print(data.get("telephone")) # TODO: check specs
        print("==================")
        email = Courriels(
            # contact = models.ForeignKey(Contacts, on_delete=models.CASCADE),
            courriel = data.get("email"),
            # ordre = models.IntegerField(null=True, blank=True)
        )
        # email.save()
        telephone = Telephones(
            # contact = models.ForeignKey(Contacts, on_delete=models.CASCADE),
            telephone = data.get("telephone"),
            # type = models.CharField(max_length=255),
            # remarque = models.CharField(max_length=255),
            # ordre = models.IntegerField()
        )
        # telephone.save()
        adherent = Adherents(
            categorie=Categories.objects.get(id=data.get("categorie")),
            poste=Postes.objects.get(id=data.get("dirigeant")),
            login=data.get("nom", "").lower() + "." + data.get("prenom", "").lower(),
            mdp="123",
            nom=data.get("nom"),
            prenom=data.get("prenom"),
            no_licence=data.get("no_licence"),
            date_naissance=data.get("date_naissance"),
            genre=data.get("genre"),
            surclassement=0,
            habilitation=data.get("habilitation"),
            arbitre=data.get("arbitre", False),
            entraineur=False,
        )
        # adherent = Adherents(
        #     id=item[0],
        #     categorie=noneReplace(Categories, item[1]),
        #     poste=noneReplace(Postes, item[2]),
        #     login=item[3],
        #     mdp=item[4],
        #     nom=item[5],
        #     prenom=item[6],
        #     no_licence=item[7],
        #     date_naissance=item[8],
        #     genre=item[9],
        #     surclassement=item[10],
        #     habilitation=item[11],
        #     arbitre=item[12],
        #     entraineur=item[13],
        # )
        print(adherent)
        # adherent.save()
        # print(adherent)


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
