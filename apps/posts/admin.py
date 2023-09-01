from django.contrib import admin

from apps.posts.models import Post


@admin.action(description='Mark as sent')
def make_available(modeladmin, request, queryset):
    queryset.update(status='sent')


@admin.action(description='Mark as not sent')
def make_unavailable(modeladmin, request, queryset):
    queryset.update(status='not_sent')


class PostAdmin(admin.ModelAdmin):
    actions = [make_available, make_unavailable]
    list_display = ['title', 'content', 'status']
    list_display_links = ['title', 'content']
    list_filter = ['status']
    search_fields = ['title']


admin.site.register(Post, PostAdmin)
