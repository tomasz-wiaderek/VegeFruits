from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, profile
from .views import UserLocationCreateView, UserLocationUpdateView

app_name = 'user_man'
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('profile/', profile, name='profile'),
    path('location/create/', UserLocationCreateView.as_view(), name='location-create'),
    path('location/<int:pk>/update/', UserLocationUpdateView.as_view(), name='location-update'),
]



