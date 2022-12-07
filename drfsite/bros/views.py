from django.shortcuts import render
from rest_framework import generics
from .models import Bros
from .serializers import BrosSerializer


class BrosAPIView(generics.ListAPIView):
    queryset = Bros.objects.all()
    serializer_class = BrosSerializer
