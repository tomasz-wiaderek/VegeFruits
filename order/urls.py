from django.urls import path
from .views import create_order, finalise_order, MyOrdersListView, OrderDetailView


app_name = 'order'
urlpatterns = [
    path('create/<int:pk>', create_order, name='create'),
    path('summary/<int:pk>', finalise_order, name='finalise'),
    path('myorders/', MyOrdersListView.as_view(), name='myorders'),
    path('detail/<int:pk>', OrderDetailView.as_view(), name='detail')
]
