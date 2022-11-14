from rest_framework import serializers
from .models import Inventory, Supplier


class InventorySerializer(serializers.ModelSerializer):
    supplier = serializers.ReadOnlyField(source='supplier.name')  # Return the supplier name instead of id

    class Meta:
        model = Inventory
        fields = ['id', 'name', 'supplier', 'availability']
