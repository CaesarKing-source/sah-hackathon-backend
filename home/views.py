from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import serializers
from home.serializers import HackathonSerializer
from home.serializers import ContactSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from django.http import JsonResponse
from rest_framework import generics

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the home index.")

@permission_classes((AllowAny,))
class HackathonView(generics.CreateAPIView):
    serializer_class = HackathonSerializer
    
    def post(self, request):
        serializer = HackathonSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    
@permission_classes((AllowAny,))
class ContactView(generics.CreateAPIView):
    serializer_class = ContactSerializer
    
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
        



