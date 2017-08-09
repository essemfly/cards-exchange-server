from rest_framework import serializers
from dogs.models import Dogs


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dogs
        fields = '__all__'
