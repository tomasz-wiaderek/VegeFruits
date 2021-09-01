from django.shortcuts import render, redirect, reverse

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
        return redirect('/')
    context = {
        'order': current_order,
        'orderlines': orderlines,
    }
    return render(request, 'order/finalise.html', context=context)
