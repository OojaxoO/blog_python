from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from user.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['get'])
    def userinfo(self, request):
        """
        用户信息
        :param: request.
        :return: User
        """
        user = self.request.user
        serializer = UserSerializer(user)
        return Response({"data": serializer.data})
