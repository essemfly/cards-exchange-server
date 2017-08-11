from rest_framework.views import APIView
from rest_framework import permissions
from django.shortcuts import redirect
from rest_framework.response import Response
from dogs.serializers import DogsImageSerializer
from dogs.models import DogsImage
import random


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


class DogsImageResponse(APIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def post(self, request):
        images = list(DogsImage.objects.all())
        random.shuffle(images)
        ret = {
            "message": {
                "text": '',
                "photo": {
                    "url": "http://api.essemfly.com" + images[0].datafile.url,
                    #"url": "http://placekitten.com/640/480",
                    "width": 640,
                    "height": 480,
                }
            },
            "keyboard": {
                "type": "buttons",
                "buttons": [
                    "사진보기",
                ]
            }
        }
        return Response(ret)


class DogsKeyboard(APIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def get(self, request):
        ret = {
            "type": "buttons",
            "buttons": [
                "사진보기",
            ]
        }
        return Response(ret)
