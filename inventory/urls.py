from django.urls import path
from .views import InventoryCreateView, InventoryUpdateView, list_profiles_inventories

app_name = 'inventory'
urlpatterns = [
    path('create/', InventoryCreateView.as_view(), name='create'),
    path('myinventory/', list_profiles_inventories, name='myinventory'),
    path('<int:pk>/update/', InventoryUpdateView.as_view(), name='update')
]
