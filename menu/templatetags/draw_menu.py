from django import template

from menu.models import Item
from menu.templatetags.lib import get_item_ids_hierarchy, get_child_items

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):

    selected_item_id = context.get('selected_item_id')
    selected_item_id = int(selected_item_id) if selected_item_id else None

    menu_items = Item.objects.values('id', 'name', 'parent_item_id', 'menu__id', 'menu__name').filter(
        menu__name=menu_name).all()  # all items for current menu

    item_ids_hierarchy = get_item_ids_hierarchy(menu_items, selected_item_id)

    menu_result_dict = dict(name=menu_name)
    menu_root_dir_items = list(filter(lambda i: not i['parent_item_id'], menu_items))
    # menu_root_dir_items - only root directory items. Child items added in the next loop if need.

    for item in menu_root_dir_items:
        item['selected'] = True if item['id'] == selected_item_id else False
        item['child_items'] = get_child_items(menu_items, item['id'], selected_item_id, item_ids_hierarchy)
    menu_result_dict['items'] = menu_root_dir_items
    return menu_result_dict

