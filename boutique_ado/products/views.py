from django.shortcuts import render
from .models import Product


def all_products(request):
    """returns all products - sorting and search"""

    products = Product.objects.all()

    context = {
        "products": products,
    }
    return render(request, "products/products.html", context)
