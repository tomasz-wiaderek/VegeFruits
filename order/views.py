from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.forms import inlineformset_factory
from .models import Order, OrderLine
from user_management.models import Profile
from inventory.models import Inventory


def create_order(request, pk):
    current_order = Order.objects.filter(status='unposted',
                                         customer=request.user)
    producer = Profile.objects.get(pk=pk)
    inventories = Inventory.objects.filter(profile=producer)

    if current_order.exists():
        current_order = current_order[0]
    else:
        current_order = Order.objects.create(customer=request.user)

    OrderLineFormset = inlineformset_factory(Order,
                                             OrderLine,
                                             fields=('inventory', 'quantity',),
                                             extra=len(inventories))
    formset = OrderLineFormset(queryset=OrderLine.objects.none(), instance=current_order)
    if request.method == 'POST':
        formset = OrderLineFormset(request.POST, instance=current_order)
        if formset.is_valid():
            formset.save()
            return redirect(reverse('order:finalise', kwargs={'pk': current_order.pk}))

    context = {
        'order': current_order,
        'producer': producer,
        'formset': formset
    }
    return render(request, 'order/create.html', context=context)


def finalise_order(request, pk):
    current_order = Order.objects.get(pk=pk)
    orderlines = OrderLine.objects.filter(order=current_order)
    if request.method == 'POST':
        current_order.status = 'unconfirmed'
        current_order.save()
        return redirect('order:myorders')
    context = {
        'order': current_order,
        'orderlines': orderlines,
    }
    return render(request, 'order/finalise.html', context=context)


class MyOrdersListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'order/my_orders.html'

    def get_queryset(self):
        """Return all Orders for current user that are not with 'unposted' status."""
        profile = Profile.objects.get(user=self.request.user)
        if profile.profile_type == 'producer':
            queryset = Order.objects.filter(orderline__inventory__profile=profile).exclude(status='unposted')
        else:
            queryset = Order.objects.filter(customer=profile.user).exclude(status='unposted')
        return set(queryset)


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orderlines'] = OrderLine.objects.filter(order=self.object)
        return context
