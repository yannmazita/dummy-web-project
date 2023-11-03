# parsing data from the client
from rest_framework.parsers import JSONParser

# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt

# for sending response to the client
from django.http import HttpResponse, JsonResponse

# API definition for task
from .serializers import MemberSerializer

# Model
from .models import Adherents, Equipes


@csrf_exempt
def adherents(request):
    """Break GDPR"""
    if request.method == "GET":
        adherents = Adherents.objects.all()  # type: ignore
        serializer = MemberSerializer(adherents, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = MemberSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def equipes(request):
    if request.method == "GET":
        equipes = Equipes.objects.all()  # type: ignore
        serializer = MemberSerializer(equipes, many=True)
        return JsonResponse(serializer.data, safe=False)
