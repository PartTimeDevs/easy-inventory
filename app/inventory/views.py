# Create your views here.
from django.http import JsonResponse
from django.views.generic import ListView
from inventory.models import Product


class ProductList(ListView):
    model = Product
    context_object_name = "products"


def get_products(request):
    """List products"""
    products = list(Product.objects.values())

    return JsonResponse(products, safe=False)  # or JsonResponse({'data': data})
