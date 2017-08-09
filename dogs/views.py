from rest_framework.views import APIView
from rest_framework.response import Response

from dogs.models import Dogs
from dogs.serializers import DogSerializer


class DogsList(APIView):
    def get(self, request):
        dogs = Dogs.objects.order_by('created_at').all()
        serialized = DogSerializer(dogs, many=True)
        return Response(serialized.data)
