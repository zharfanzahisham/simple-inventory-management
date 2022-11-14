from django.shortcuts import render, redirect
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Inventory, Supplier
from .serializer import InventorySerializer
from django.views import View
from django.http import Http404

# Create your views here.


class InventoryAPI(ListAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

    def list(self, request):
        # Get the name parameter
        name = request.GET.get('name')
        if name:
            # Filter in the queryset that contains the given name
            queryset = self.get_queryset(contains_name=name)
        else:
            # Get the whole queryset
            queryset = self.get_queryset()

        # Serializer and return the queryset
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self, contains_name=None):
        if contains_name:
            return self.queryset.filter(name__contains=contains_name)
        return self.queryset.all()


class InventoryListPage(View):
    template_name = 'inventory/inventory_list.html'

    def get(self, request):
        return render(request, self.template_name)


class InventoryPage(View):
    template_name = 'inventory/inventory.html'

    def get(self, request, id):
        try:
            # Search for the Inventory object with the given id
            inventory = Inventory.objects.get(id=id)
        except Inventory.DoesNotExist:
            # Inventory with the given id is not found
            return Http404
        else:
            # Pass the inventory to the context
            context = {'inventory': inventory}
            return render(request, self.template_name, context)
