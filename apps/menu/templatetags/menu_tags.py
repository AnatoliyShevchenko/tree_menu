# Django
from django import template
from django.utils.safestring import mark_safe
from django.template.context import RequestContext
from django.db.models import Q

# Local
from menu.models import MenuItem


register = template.Library()


def render_items(items: list):
    html = "<ul>"
    for item in items:
        html += f"<li>{item}</li>"
    html += "</ul>"
    return html

def render_categories(categories: dict, link: str):
    html = "<ul>"
    for key, value in categories.items():
        category_link = f"{link}{key}/"
        html += f"<li><a href='{category_link}'>{key}</a>"
        html += f"<p class='toggle-submenu'> +</p>"
        html += render_items(items=value)
        html += "</li>"
    html += "</ul>"
    return html

@register.simple_tag(takes_context=True)
def draw_menu(context: RequestContext):
    menu_name = context.get("menu_name")
    category_name = context.get("category_name")
    path = context.request.path
    menu_html = ""

    try:
        if not menu_name:
            data = MenuItem.objects.select_related(
                'category', 'menu'
            ).all().values("title", "category__title", "menu__name")
            menu_html = ""
            result = {}
            for item in data:
                category = item.get("category__title")
                menu = item.get("menu__name")
                item_title = item.get("title")
                if menu not in result:
                    result[menu] = {}
                if category not in result[menu]:
                    result[menu][category] = []
                result[menu][category].append(item_title)
            
            for menu, categories in result.items():
                link = f"/{menu}/"
                is_active = link == path
                active = ' class="active"' if is_active else ''
                menu_html += f"<li{active}><a href='{link}'>{menu}</a>"
                menu_html += f"<p class='toggle-submenu'> +</p>"
                menu_html += render_categories(
                    categories=categories, link=link
                )

        elif menu_name and not category_name:
            data = MenuItem.objects.select_related(
                'category'
            ).filter(
                menu__name=menu_name
            ).values("category__title", "title")
            result = {}
            for item in data:
                category = item.get("category__title")
                item_title = item.get("title")
                if category not in result:
                    result[category] = []
                result[category].append(item_title)
            
            link = f"/{menu_name}/"
            menu_html += render_categories(
                categories=result, link=link
            )
        
        elif menu_name and category_name:
            data = MenuItem.objects.filter(
                Q(menu__name=menu_name) & Q(category__title=category_name)
            ).values("title")
            menu_html = ""
            result = []
            for item in data:
                result.append(item.get("title"))

            link = f"/{menu_name}/{category_name}/"
            menu_html += render_items(items=result)

        return mark_safe(f"<ul>{menu_html}</ul>")

    except MenuItem.DoesNotExist:
        return ""
