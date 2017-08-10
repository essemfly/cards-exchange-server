from rest_framework import serializers
from dogs.models import DogsImage


class DogsImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DogsImage
        fields = '__all__'

    def save(self, validated_data):
        dog_image = DogsImage.objects.create(
            name=validated_data['name'],
            datafile=validated_data['datafile'],
            description=validated_data['description'],
        )
        dog_image.save()
        return dog_image