from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, viewsets

from .models import Bros, Category
from .serializers import BrosSerializer


class BrosViewSet(viewsets.ModelViewSet):
    # queryset = Bros.objects.all()
    serializer_class = BrosSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        if not pk:
            return Bros.objects.all()[:3]

        return Bros.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})

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
