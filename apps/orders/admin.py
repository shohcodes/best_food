from django.contrib import admin

from apps.orders.models import Order, OrderFood


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'telegram_user', 'status']
    list_display_links = ['id', 'telegram_user']
    search_fields = ['telegram_user', 'delivered_by']
    list_filter = ['status']
    fieldsets = [
        (
            'Main Info',
            {
                'fields': ['total_price', 'telegram_user', 'status']
            }
        ),
        (
            'Extra Info',
            {
                'fields': ['description', 'delivered_by', 'delivered_at']
            }
        ),
        (
            'Locations',
            {
                'fields': ['lat', 'lon']
            }
        )
    ]


class OrderFoodAdmin(admin.ModelAdmin):
    list_display = ['order', 'food', 'amount', 'price']
    list_display_links = ['order', 'food']
    search_fields = ['food']


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderFood)
