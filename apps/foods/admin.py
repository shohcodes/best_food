from django.contrib import admin

from apps.foods.models import Food, Category

admin.site.register(Food)
admin.site.register(Category)
