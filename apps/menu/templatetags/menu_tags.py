# Django
from django import template
from django.utils.safestring import mark_safe
from django.db.models import QuerySet
from django.template.context import RequestContext

# Local
from menu.models import Menu, MenuItem


register = template.Library()


def render_menu(items: QuerySet[MenuItem], prefix: str, parent=None):
    html = "<ul>"
    for item in items:
        if item.parent == parent:
            html += f"<li><a href='{prefix}/{item.title}'>{item.title}</a>"
            children = render_menu(items=items, prefix=prefix, parent=item)
            if children:
                html += children
            html += "</li>"
    html += "</ul>"
    return html

@register.simple_tag(takes_context=True)
def draw_menu(context: RequestContext):
    path = context.request.path
    try:
        if path != "/":
            temp = path.split("/")
            menu = Menu.objects.prefetch_related("items").get(name=temp)
            items = menu.items.all()
            menu_html = render_menu(items=items, prefix=temp)
        else:
            menus = Menu.objects.prefetch_related("items").all()
            menu_html = ""
            for menu in menus:
                items = menu.items.all()
                menu_html += f"<li><a href='{menu.name}'>{menu.name}</a>"
                menu_html += render_menu(items=items, prefix=menu.name)
                
        return mark_safe(menu_html)

    except Menu.DoesNotExist:
        return ""
