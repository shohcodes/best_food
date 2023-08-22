from rest_framework import serializers
from apps.users.models import User, TelegramUser


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        exclude = ['created_at', 'updated_at']


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TelegramUserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = '__all__'
        exclude = ['created_at', 'updated_at']


class TelegramUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = '__all__'
