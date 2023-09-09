from django.db import models

from apps.foods.models import Food
from apps.users.models import TelegramUser, User
from apps.orders.choices import StatusChoices, OrderTypeChoices, PaymentTypeChoices


class Order(models.Model):
    total_price = models.FloatField()
    telegram_user = models.ForeignKey(TelegramUser, related_name='orders_tg_users', on_delete=models.CASCADE)
    lat = models.FloatField(default=0)
    lon = models.FloatField(default=0)
    description = models.TextField(null=True)
    payment_type = models.CharField(max_length=20, choices=PaymentTypeChoices.choices, default=PaymentTypeChoices.CASH)
    delivered_by = models.ForeignKey(User, related_name='deliverer_order', on_delete=models.CASCADE)
    delivery_price = models.FloatField(default=0)
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.NEW)
    order_type = models.CharField(max_length=255, choices=OrderTypeChoices.choices, default=OrderTypeChoices.TAKE_AWAY)
    takeaway_time = models.PositiveIntegerField(default=0)
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
    order = models.ForeignKey(Order, related_name='order_number', on_delete=models.PROTECT)
    food = models.ForeignKey(Food, related_name='foods_in_order', on_delete=models.PROTECT)
    amount = models.PositiveSmallIntegerField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.order}"
