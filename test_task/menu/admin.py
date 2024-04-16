from django.contrib import admin
from .models import MenuItem


class MenuItemAdmin(admin.ModelAdmin):
    list_display: tuple = 'name', 'url', 'named_url', 'parent'
    list_filter: tuple = 'name',
    search_fields: tuple = 'name', 'url', 'named_url'
    ordering: tuple = 'name', 'id'


admin.site.register(MenuItem, MenuItemAdmin)