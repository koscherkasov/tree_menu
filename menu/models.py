from django.db import models

# Create your models here.


class Menu(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.name)


class Item(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    parent_item = models.ForeignKey('self', null=True, blank=True)

    def __str__(self):
        if self.parent_item:
            return '{} -> {}'.format(self.parent_item, self.name)
        return 'menu({}) |-> {}'.format(self.menu, self.name)
