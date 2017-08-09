from django.http import Http404
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response

from account.serializers import AccountSerializer


class UserDetail(APIView):
    @staticmethod
    def get_object(pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, pk):
        user = self.get_object(pk)
        serializer = AccountSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        serialized = AccountSerializer(user, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


class UserRegister(APIView):
    user_model = get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]

    def post(self, request):
        valid_user_fields = [f.name for f in self.user_model._meta.fields]
        defaults = {
            'first_name': '',
            'last_name': '',
        }
        serialized = AccountSerializer(data=request.data)
        if serialized.is_valid():
            user_data = {field: data for (field, data) in request.data.items() if field in valid_user_fields}
            user_data.update(defaults)
            user = serialized.create(user_data)
            return Response(AccountSerializer(instance=user).data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
