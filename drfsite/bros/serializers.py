from rest_framework import serializers
from .models import Bros


class BrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bros
        fields = ('title', 'cat_id')
