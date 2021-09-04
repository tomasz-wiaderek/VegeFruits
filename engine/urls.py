from django.urls import path
from .views import home_search

app_name = 'engine'
urlpatterns = [
    path('', home_search, name='home'),
]
