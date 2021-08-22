from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import Http404

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import CreateView, UpdateView
from .models import ProfileLocation, ProfileAdditionalInfo
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, \
    ProfileLocationModelForm, ProfileAdditionalInfoModelForm


# User and Profile views

def register(request):
    """Create new User and Profile."""

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
    """Display profile of logged in User"""

    user_profile = request.user.profile
    try:
        info = get_object_or_404(ProfileAdditionalInfo, profile=user_profile)
    except Http404:
        info = 'This section is empty.'
    try:
        location = get_object_or_404(ProfileLocation, profile=user_profile)
    except Http404:
        location = 'Location was not specified.'

    context = {
        'user': request.user,
        'user_profile': user_profile,
        'location': location,
        'info': info
    }
    return render(request, 'profile/profile.html', context=context)


@login_required
def profile_update(request):
    """Update profile of logged in User."""

    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            messages.success(request, f'Your account has been updated.')
            return redirect('user_man:profile')
    else:
        user_update_form = UserUpdateForm(instance=request.user)
        profile_update_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'user_update_form': user_update_form,
        'profile_update_form': profile_update_form
    }
    return render(request, 'profile/profile_update.html', context=context)


# ProfileLocation class views

class ProfileLocationCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    template_name = 'profile/profile_location.html'
    queryset = ProfileLocation.objects.all()
    form_class = ProfileLocationModelForm

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)


class ProfileLocationUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    template_name = 'profile/profile_location.html'
    queryset = ProfileLocation.objects.all()
    form_class = ProfileLocationModelForm

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)


# ProfileAdditionalInfo class views

class ProfileInfoCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    template_name = 'profile/profile_info.html'
    queryset = ProfileAdditionalInfo.objects.all()
    form_class = ProfileAdditionalInfoModelForm

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)


class ProfileInfoUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    template_name = 'profile/profile_info.html'
    queryset = ProfileAdditionalInfo.objects.all()
    form_class = ProfileAdditionalInfoModelForm

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)
