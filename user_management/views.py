from django.shortcuts import render

from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from .models import User
# Create your views here.


class UserDetailView(DetailView):
    template_name = 'user/user_detail.html'
    queryset = User.objects.all()
#  jak wstawic informacje o lokalizacji ?


class UserListView(ListView):
    template_name = 'user/user_list.html'
    queryset = User.objects.all()

