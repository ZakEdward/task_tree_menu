from django.shortcuts import render
from .models import MenuItem


def draw_menu(request, menu_name):
    menu_items: MenuItem = MenuItem.objects.filter(name=menu_name).select_related('parent')
    return render(request, 'menu/page.html', {'menu_items': menu_items})

