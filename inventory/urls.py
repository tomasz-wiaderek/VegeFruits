from django.urls import path
from .views import InventoryCreateView, InventoryUpdateView, InventoryListView, SelectedProducerInventoryListView

app_name = 'inventory'
urlpatterns = [
    path('create/', InventoryCreateView.as_view(), name='create'),
    path('myinventory/', InventoryListView.as_view(), name='myinventory'),
    path('<int:pk>/update/', InventoryUpdateView.as_view(), name='update'),
    path('<int:pk>/', SelectedProducerInventoryListView.as_view(), name='selected-producer-inventory')
]
