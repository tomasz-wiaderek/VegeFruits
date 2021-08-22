from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, profile, profile_update, \
    ProfileLocationCreateView, ProfileLocationUpdateView, ProfileInfoCreateView, ProfileInfoUpdateView


app_name = 'user_man'
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('profile/', profile, name='profile'),
    path('profile/update/', profile_update, name='profile-update'),
    path('profile/loc/create/', ProfileLocationCreateView.as_view(), name='location-create'),
    path('profile/loc/<int:pk>/update/', ProfileLocationUpdateView.as_view(), name='location-update'),
    path('profile/info/create/', ProfileInfoCreateView.as_view(), name='info-create'),
    path('profile/info/<int:pk>/update/', ProfileInfoUpdateView.as_view(), name='info-update'),

]



