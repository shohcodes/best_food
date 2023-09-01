from django.contrib import admin

from apps.users.models import User, TelegramUser


class UserAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'role']
    list_display_links = ['firstname', 'lastname']
    search_fields = ['firstname', 'lastname']
    list_filter = ['role']
    fieldsets = [
        (
            'Personal Information',
            {
                'fields': ['firstname', 'lastname']
            }
        ),
        (
            'Role',
            {
                'fields': ['role']
            }
        )
    ]


@admin.action(description='Block selected')
def block_selected(modeladmin, request, queryset):
    queryset.update(is_blocked=True)


@admin.action(description='Unblock selected')
def unblock_selected(modeladmin, request, queyset):
    queyset.update(is_blocked=False)


class TelegramUserAdmin(admin.ModelAdmin):
    actions = [block_selected, unblock_selected]
    list_display = ['fullname', 'is_verified', 'chat_id', 'is_blocked']
    search_fields = ['fullname', 'chat_id']
    list_filter = ['is_verified', 'is_blocked']
    fieldsets = [
        (
            'Personal Information',
            {
                'fields': ['fullname', 'chat_id']
            }
        ),
        (
            'Status',
            {
                'fields': ['is_verified', 'is_blocked']
            }
        ),
        (
            'Contacts',
            {
                'fields': ['phone_number']
            }
        )
    ]


admin.site.register(User, UserAdmin)
admin.site.register(TelegramUser, TelegramUserAdmin)
