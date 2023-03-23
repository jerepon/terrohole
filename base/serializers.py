from .models import HorrorStory
from rest_framework import serializers


class HorrorStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HorrorStory
        fields = '__all__'