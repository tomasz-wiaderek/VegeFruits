from django.shortcuts import render, reverse
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Inventory
from .forms import InventoryModelForm


@login_required()
def list_profiles_inventories(request):
    queryset = Inventory.objects.filter(profile=request.user.profile)
    context = {
        'object_list': queryset,
        'profile': request.user.profile
    }
    return render(request, 'inventory/myinventory.html', context=context)


class InventoryCreateView(LoginRequiredMixin, CreateView):
    model = Inventory
    form_class = InventoryModelForm
    template_name = 'inventory/update.html'

    def get_success_url(self):
        return reverse('inventory:myinventory')

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)


class InventoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Inventory
    form_class = InventoryModelForm
    template_name = 'inventory/update.html'

    def get_success_url(self):
        return reverse('inventory:myinventory')
