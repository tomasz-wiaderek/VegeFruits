from django.shortcuts import render, get_object_or_404, reverse
from inventory.models import Inventory
from .models import Order, OrderLine


def add_to_order(request, pk):
    item = get_object_or_404(Inventory, pk=pk)
    order_queryset = Order.objects.filter(user=request.user, status='unposted')
    if not order_queryset.exists():
        order = Order.objects.create(customer=request.user)
    else:
        order = order_queryset[0]
    order_line = OrderLine.objects.create(inventory=item, order=order)
    return reverse('inventory:selected-producer-inventory')