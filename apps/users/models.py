from django.db import models


class RoleChoices(models.TextChoices):
    ADMIN = ('admin',)
    ORDER_TAKER = ('order_taker',)
    DELIVERER = ('deliverer',)


class User(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    role = models.CharField(max_length=20, choices=RoleChoices.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'{self.firstname} {self.lastname}'


class TelegramUser(models.Model):
    chat_id = models.IntegerField()
    phone_number = models.CharField(max_length=13)
    fullname = models.CharField(max_length=244)
    role = models.CharField(max_length=11, choices=RoleChoices.choices)
    is_blocked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'TelegramUser'
        verbose_name_plural = 'TelegramUsers'

    def __str__(self):
        return self.fullname
