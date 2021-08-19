from django.urls import path

from .views import register
from .views import UserLocationCreateView, UserLocationUpdateView

app_name = 'user_man'
urlpatterns = [
    path('register/', register, name='register'),
    # path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    # path('user/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    # path('user/<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),
    path('location/create/', UserLocationCreateView.as_view(), name='location-create'),
    path('location/<int:pk>/update/', UserLocationUpdateView.as_view(), name='location-update'),
]



