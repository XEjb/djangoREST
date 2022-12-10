from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, viewsets

from .models import Bros
from .serializers import BrosSerializer


class BrosViewSet(viewsets.ModelViewSet):
    queryset = Bros.objects.all()
    serializer_class = BrosSerializer


# class BrosAPIList(generics.ListCreateAPIView):
#     queryset = Bros.objects.all()
#     serializer_class = BrosSerializer
#
#
# class BrosAPIUpdate(generics.UpdateAPIView):
#     queryset = Bros.objects.all()
#     serializer_class = BrosSerializer
#
#
# class BrosAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Bros.objects.all()
#     serializer_class = BrosSerializer
