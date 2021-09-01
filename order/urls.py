from django.urls import path
from .views import create_order,finalise_order


app_name = 'order'
urlpatterns = [
    path('create/<int:pk>', create_order, name='create'),
    path('summary/<int:pk>', finalise_order, name='finalise'),
]
