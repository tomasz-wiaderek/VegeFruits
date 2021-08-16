from django.shortcuts import render

from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from .models import User
from .forms import UserModelForm
# Create your views here.


class UserDetailView(DetailView):
    template_name = 'user/user_detail.html'
    queryset = User.objects.all()
#  jak wstawic informacje o lokalizacji ?


class UserListView(ListView):
    template_name = 'user/user_list.html'
    queryset = User.objects.all()


class UserCreateView(CreateView):
    template_name = 'user/user_create.html'
    queryset = User.objects.all()
    form_class = UserModelForm
