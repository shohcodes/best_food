from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from apps.users.models import User
from apps.users.serializers import UserDetailSerializer, UserListSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return UserListSerializer
        return UserDetailSerializer
