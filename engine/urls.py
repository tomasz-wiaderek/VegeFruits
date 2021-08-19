from django.urls import path
from .views import home

app_name = 'engine'
urlpatterns = [
    path('', home, name='page-home'),
]
