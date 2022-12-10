import io

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Bros


# class BrosModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class BrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bros
        fields = "__all__"






# def encode():
#     model = BrosModel('Nik', 'Content: Nik')
#     model_sr = BrosSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Nik","content":"Content: Nik"}')
#     data = JSONParser().parse(stream)
#     serializer = BrosSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
