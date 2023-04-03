from django.contrib import admin

from items.models import Inventory, Items


admin.site.register(Inventory)
admin.site.register(Items)

