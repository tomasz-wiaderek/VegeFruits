from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from .models import User, UserLocation
from .forms import UserModelForm, UserLocationModelForm
# Create your views here.


# User class views

class UserDetailView(DetailView):
    template_name = 'user/user_detail.html'
    queryset = User.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['location'] = UserLocation.objects.get(user=context['object'])
        return context


class UserListView(ListView):
    template_name = 'user/user_list.html'
    queryset = User.objects.all()


class UserCreateView(CreateView):
    template_name = 'user/user_create.html'
    queryset = User.objects.all()
    form_class = UserModelForm


class UserUpdateView(UpdateView):
    template_name = 'user/user_create.html'
    queryset = User.objects.all()
    form_class = UserModelForm


class UserDeleteView(DeleteView):
    template_name = 'user/user_delete.html'
    queryset = User.objects.all()

    def get_success_url(self):
        return reverse('user:users-list')


# UserLocation class views

class UserLocationCreateView(CreateView):
    template_name = 'user_location/ul_create.html'
    queryset = UserLocation.objects.all()
    form_class = UserLocationModelForm


class UserLocationUpdateView(UpdateView):
    template_name = 'user_location/ul_create.html'
    queryset = UserLocation.objects.all()
    form_class = UserLocationModelForm


class UserLocationDeleteView(DeleteView):
    template_name = 'user_location/ul_delete.html'
    queryset = UserLocation.objects.all()

    def get_success_url(self):
        return reverse('user:users-list')


class UserLocationDetailView(DetailView):
    template_name = 'user_location/ul_detail.html'
    queryset = UserLocation.objects.all()
