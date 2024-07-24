# Django
from django import template
from django.utils.safestring import mark_safe

# Local
from menu.models import Menu, MenuItem


register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    try:
        menu = Menu.objects.get(name=menu_name)
        items = menu.items.all()
        current_url = context['request'].path

        def render_menu(items, parent=None):
            html = '<ul>'
            for item in items:
                if item.parent == parent:
                    html += f'<li><a href="{item.get_absolute_url()}">{item.title}</a>'
                    children = render_menu(items, item)
                    if children:
                        html += children
                    html += '</li>'
            html += '</ul>'
            return html

        menu_html = render_menu(items)
        return mark_safe(menu_html)

    except Menu.DoesNotExist:
        return ''
