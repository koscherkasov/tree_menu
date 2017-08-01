def get_item_by_id(items, id):
    """Get item by id if exist. Otherwise return None"""
    items = list(filter(lambda i: i['id'] == id, items))
    if not items:
        return None
    return items[0]


def get_parent_item(items, item_id):
    """Get parent item for item_id if parent exist. Otherwise return None"""
    selected_item = get_item_by_id(items, item_id)
    return selected_item['parent_item_id'] if selected_item else None


def get_item_ids_hierarchy(items, selected_item_id):
    """Get list of item ids which include all items from selected to root"""
    parent_item_id = get_parent_item(items, selected_item_id)
    item_ids_hierarchy = [selected_item_id] if selected_item_id else []
    while parent_item_id:
        item_ids_hierarchy.append(parent_item_id)
        parent_item_id = get_parent_item(items, parent_item_id)
    return item_ids_hierarchy


def get_child_items(items, current_item_id, selected_item_id, item_ids_hierarchy):
    """Get child items for current_item_id"""
    if current_item_id not in item_ids_hierarchy:
        return []
    child_items = list(filter(lambda i: i['parent_item_id'] == current_item_id, items))
    for item in child_items:
        item['selected'] = True if item['id'] == selected_item_id else False
        item['child_items'] = get_child_items(items, item['id'], selected_item_id, item_ids_hierarchy)
    return child_items
