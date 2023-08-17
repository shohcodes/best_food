from django.db import models

from apps.foods.models import Food
from apps.users.models import TelegramUser, User


class StatusChoices(models.TextChoices):
    NEW = ('new',)
    PREPARING = ('preparing',)
    PREPARED = ('prepared',)
    DELIVERING = ('delivering',)
    DELIVERED = ('delivered',)
    CANCELED = ('canceled',)


class Order(models.Model):
    total_price = models.FloatField()
    telegram_user = models.ForeignKey(TelegramUser, related_name='orders_tg_users', on_delete=models.CASCADE)
    lat = models.DecimalField(decimal_places=10, max_digits=1000)
    lon = models.DecimalField(decimal_places=10, max_digits=1000)
    description = models.TextField(null=True)
    delivered_by = models.ForeignKey(User, related_name='deliverer_order', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=StatusChoices.choices)
    foods = models.ManyToManyField(Food, "oder_foods", through="OrderFood")
    delivered_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f"{self.id}"


class OrderFood(models.Model):
    order = models.ForeignKey(Order, related_name='order_number', on_delete=models.CASCADE)
    food = models.ForeignKey(Food, related_name='foods_in_order', on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.order}"
