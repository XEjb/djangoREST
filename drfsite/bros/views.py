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
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Bros.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = BrosSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

# class BrosAPIView(generics.ListAPIView):
#     queryset = Bros.objects.all()
#     serializer_class = BrosSerializer
