from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, viewsets

from .models import Bros, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import BrosSerializer


class BrosAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000


class BrosAPIList(generics.ListCreateAPIView):
    queryset = Bros.objects.all()
    serializer_class = BrosSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = BrosAPIListPagination


class BrosAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Bros.objects.all()
    serializer_class = BrosSerializer
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication, )


class BrosAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Bros.objects.all()
    serializer_class = BrosSerializer
    permission_classes = (IsAdminOrReadOnly,)
