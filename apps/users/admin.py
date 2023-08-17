from django.contrib import admin

from apps.users.models import User, TelegramUser

admin.site.register(User)
admin.site.register(TelegramUser)
