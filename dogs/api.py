from rest_framework.views import APIView
from rest_framework import permissions
from django.shortcuts import redirect

from dogs.serializers import DogsImageSerializer


class DogsImageRegister(APIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def post(self, request):
        serializer = DogsImageSerializer()
        print(len(request.FILES.getlist('images')))


        for img_file in request.FILES.getlist('images'):
            dog_image_data = {
                'name': request.data.get('name'),
                'datafile': img_file,
                'description': 'test for description',
            }

            serializer.save(dog_image_data)

        return redirect('/dogs/register')
