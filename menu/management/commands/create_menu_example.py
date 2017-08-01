from django.core.management.base import BaseCommand, CommandError
from menu.models import Menu, Item

FIRST_MENU_NAME = 'food'
SECOND_MENU_NAME = 'drinks'

FIRST_MENU_ROOT_ITEM_NAMES = ['sweets', 'fruit', 'vegetables']
FIRST_MENU_1_LEVEL_NAMES, PARENT_INDEX_FOR_1_LEVEL = ['banana', 'orange', 'strawberry'], 1
FIRST_MENU_2_LEVEL_NAMES, PARENT_INDEX_FOR_2_LEVEL = ['old', 'new'], 0

SECOND_MENU_ROOT_ITEM_NAMES = ['cola', 'juice']


class Command(BaseCommand):
    help = 'Quick create two menus'

    def handle(self, *args, **options):

        # FIRST MENU
        menu = Menu(name=FIRST_MENU_NAME)
        menu.save()
        # root
        root_items = []
        for root_item_name in FIRST_MENU_ROOT_ITEM_NAMES:
            item = Item(menu=menu, name=root_item_name)
            item.save()
            root_items.append(item)
        # first level
        first_level_items = []
        parent_item = root_items[PARENT_INDEX_FOR_1_LEVEL]
        for item_name in FIRST_MENU_1_LEVEL_NAMES:
            item = Item(menu=menu, name=item_name, parent_item=parent_item)
            item.save()
            first_level_items.append(item)
        # second level
        parent_item = first_level_items[PARENT_INDEX_FOR_2_LEVEL]
        for item_name in FIRST_MENU_2_LEVEL_NAMES:
            item = Item(menu=menu, name=item_name, parent_item=parent_item)
            item.save()
        self.stdout.write(self.style.SUCCESS('Successfully created menu {}'.format(menu.name)))

        # SECOND MENU
        menu = Menu(name=SECOND_MENU_NAME)
        menu.save()
        # root
        root_items = []
        for root_item_name in SECOND_MENU_ROOT_ITEM_NAMES:
            item = Item(menu=menu, name=root_item_name)
            item.save()
            root_items.append(item)
        self.stdout.write(self.style.SUCCESS('Successfully created menu {}'.format(menu.name)))
