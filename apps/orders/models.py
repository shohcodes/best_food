from django.db import models

from apps.users.models import TelegramUser, User


class StatusChoices(models.Choices):
    DELIVERED = ('delivered',)
    NOT_DELIVERED = ('not_delivered',)


class Order(models.Model):
    total_price = models.FloatField()
    telegram_user = models.ForeignKey(TelegramUser, related_name='orders_tg_users', on_delete=models.CASCADE)
    lat = models.DecimalField()
    lon = models.DecimalField()
    description = models.TextField()
    delivered_by = models.ForeignKey(User, related_name='orders_users', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=StatusChoices.choices)
    delivered_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.description


class OrderFood(models.Model):
    pass
