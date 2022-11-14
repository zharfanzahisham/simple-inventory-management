from django.urls import path
from . import views


urlpatterns = [
    path('', views.InventoryListPage.as_view(), name='inventory_list_page'),
    path('api/inventory/', views.InventoryAPI.as_view(), name='inventory_list_api'),
    path('inventory/<int:id>/', views.InventoryPage.as_view(), name='inventory_page'),
]
