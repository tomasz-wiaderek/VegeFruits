from django.urls import path
from .views import create_order


app_name = 'order'
urlpatterns = [
    path('create/<int:pk>', create_order, name='create'),
]
