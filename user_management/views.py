from django.shortcuts import render, redirect
from django.urls import reverse

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from .models import UserLocation
from .forms import UserRegisterForm, UserLocationModelForm


# User views

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Account created for {username}')
            return redirect('user_man:login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', context={'form': form})


@login_required
def profile(request):
    return render(request, 'user/profile.html', context={})


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
        return reverse('user_man:users-list')


class UserLocationDetailView(DetailView):
    template_name = 'user_location/ul_detail.html'
    queryset = UserLocation.objects.all()
