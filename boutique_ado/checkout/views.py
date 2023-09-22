from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkoutView(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': "pk_test_51NtCKUBzXpaumtPtf7mgklwmmum1ECfN6aWvHBzF2xOR63bVNSU2slSFiMpv9mTpv3nnIJZVvb8koBHNr7OMzDlQ00k4LyAsws",
        'client_secret': "test client secret",
    }

    return render(request, template, context)
