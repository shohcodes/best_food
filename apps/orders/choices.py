from django.db import models


class StatusChoices(models.TextChoices):
    NEW = ('new', 'Yangi')
    PREPARING = ('preparing', 'Tayyorlanmoqda')
    PREPARED = ('prepared', 'Tayyor')
    DELIVERING = ('delivering', 'Yetkazilmoqda')
    DELIVERED = ('delivered', 'Topshirildi')
    CANCELED = ('canceled', 'Bekor Qilindi')


class OrderTypeChoices(models.TextChoices):
    DELIVERY = ('delivery', 'Yetkazib berish')
    TAKE_AWAY = ('take_away', 'Olib ketish')


class PaymentTypeChoices(models.TextChoices):
    CASH = ('cash', 'Naqd')
    CARD = ('card', 'Karta')
