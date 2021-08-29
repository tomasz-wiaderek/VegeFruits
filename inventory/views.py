from django.shortcuts import reverse, get_object_or_404
from django.views.generic import CreateView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from user_management.models import Profile
from .models import Inventory
from .forms import InventoryModelForm


class InventoryCreateView(LoginRequiredMixin, CreateView):
    model = Inventory
    form_class = InventoryModelForm
    template_name = 'inventory/update.html'

    def get_success_url(self):
        return reverse('inventory:myinventory')

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)


class InventoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Inventory
    form_class = InventoryModelForm
    template_name = 'inventory/update.html'

    def get_success_url(self):
        return reverse('inventory:myinventory')

    def test_func(self):
        inventory = self.get_object()
        return self.request.user == inventory.profile.user


class InventoryListView(LoginRequiredMixin, ListView):
    model = Inventory
    template_name = 'inventory/my_inv.html'

    def get_queryset(self):
        profile = get_object_or_404(Profile, user=self.request.user)
        return Inventory.objects.filter(profile=profile)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.request.user.profile
        return context


class SelectedProducerInventoryListView(LoginRequiredMixin, ListView):
    model = Inventory
    template_name = 'inventory/selected_inv.html'

    def get_queryset(self):
        profile = get_object_or_404(Profile, pk=self.kwargs.get('pk'))
        return Inventory.objects.filter(profile=profile)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_object_or_404(Profile, pk=self.kwargs.get('pk'))
        return context
