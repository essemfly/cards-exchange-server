from rest_framework.views import APIView
from rest_framework import permissions
from django.shortcuts import redirect

from dogs.serializers import DogsImageSerializer


class DogsImageRegister(APIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def post(self, request):
        dog_image_data = {
            'name': request.data.get('name'),
            'datafile': request.data.get('datafile'),
            'description': 'test for description',
        }

        serializer = DogsImageSerializer()
        serializer.save(dog_image_data)

        return redirect('/dogs/register')
