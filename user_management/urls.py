from django.urls import path

from .views import UserDetailView, UserListView

app_name = 'user'
urlpatterns = [
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/', UserListView.as_view(), name='users-list'),
]

