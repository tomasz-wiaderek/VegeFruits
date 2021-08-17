from django.urls import path

from .views import UserDetailView, UserListView, UserCreateView, UserUpdateView, UserDeleteView

app_name = 'user'
urlpatterns = [
    path('users/', UserListView.as_view(), name='users-list'),
    path('create/', UserCreateView.as_view(), name='users-create'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='users-update'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='users-delete'),
]



