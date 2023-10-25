from django.shortcuts import render

# parsing data from the client
from rest_framework.parsers import JSONParser

# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt

# for sending response to the client
from django.http import HttpResponse, JsonResponse

# API definition for task
from .serializers import MemberSerializer

# Model
from .models import Member


@csrf_exempt
def members(request):
    """Break GDPR"""
    if request.method == "GET":
        members = Member.objects.all()  # type: ignore
        serializer = MemberSerializer(members, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = MemberSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def member_detail(request, pk):
    """Break GDPR"""
    try:
        member = Member.objects.get(pk=pk)  # type: ignore
    except:
        return HttpResponse(status=404)
    if request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = MemberSerializer(member, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == "DELETE":
        member.delete()
        return HttpResponse(status=204)
