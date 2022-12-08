from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import Bros
from .serializers import BrosSerializer


class BrosAPIView(APIView):
    def get(self, request):
        w = Bros.objects.all()
        return Response({'posts': BrosSerializer(w, many=True).data})

    def post(self, request):
        serializer = BrosSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = Bros.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )

        return Response({'post': BrosSerializer(post_new).data})

# class BrosAPIView(generics.ListAPIView):
#     queryset = Bros.objects.all()
#     serializer_class = BrosSerializer
