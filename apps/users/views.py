from rest_framework.viewsets import ModelViewSet

from apps.users.filters import UserRoleFilter, TelegramUserRoleFilter, TelegramUserIsBlockedFilter
from apps.users.models import User, TelegramUser
from apps.users.serializers import UserDetailSerializer, UserListSerializer, TelegramUserDetailSerializer, \
    TelegramUserListSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    filter_backends = [UserRoleFilter]

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return UserListSerializer
        return self.serializer_class


class TelegramUserViewSet(ModelViewSet):
    queryset = TelegramUser.objects.all()
    serializer_class = TelegramUserDetailSerializer
    filter_backends = [TelegramUserIsBlockedFilter, TelegramUserRoleFilter]

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return TelegramUserListSerializer
        return self.serializer_class
