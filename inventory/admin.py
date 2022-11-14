from django.contrib import admin
from .models import Inventory, Supplier

# Register your models here.


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'stock', 'availability', 'supplier')


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    pass
