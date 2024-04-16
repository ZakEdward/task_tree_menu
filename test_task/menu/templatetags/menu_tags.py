from django import template
from django.utils.safestring import mark_safe

from ..models import MenuItem

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name: str):
    menu_items: MenuItem = MenuItem.objects.filter(name=menu_name).select_related('parent')
    current_path: str = context['request'].path
    return mark_safe(_render_menu(menu_items, current_path))


def _render_menu(menu_items: MenuItem, current_path: str) -> str:
    menu_html: str = '<ul>'
    for item in menu_items:
        menu_html += '<li>'
        if item.url:
            menu_html += f'<a href="{item.url}" {"class=btn btn-primary active" if current_path == item.url + "/" else ""}>{item.name}</a>'
        else:
            menu_html += item.name
        if item.children.exists():
            menu_html += _render_menu(item.children.all(), current_path)
        menu_html += '</li>'
    menu_html += '</ul>'
    return menu_html
