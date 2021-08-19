from django.urls import path

from .views import UserDetailView, UserListView, UserCreateView, UserUpdateView, UserDeleteView, \
    UserLocationCreateView, UserLocationUpdateView

app_name = 'user_man'
urlpatterns = [
    path('users/', UserListView.as_view(), name='users-list'),
    path('user/create/', UserCreateView.as_view(), name='users-create'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('user/<int:pk>/update/', UserUpdateView.as_view(), name='users-update'),
    path('user/<int:pk>/delete/', UserDeleteView.as_view(), name='users-delete'),
    path('location/create/', UserLocationCreateView.as_view(), name='location-create'),
    path('location/<int:pk>/update/', UserLocationUpdateView.as_view(), name='location-update'),
]



