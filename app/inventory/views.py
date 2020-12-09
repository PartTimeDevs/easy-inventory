# Create your views here.
import os

from django.conf import settings
from django.core.management import call_command
from django.http import Http404, HttpResponse, JsonResponse
from django.views.generic import ListView
from inventory.models import Product


class ProductList(ListView):
    model = Product
    context_object_name = "products"


def get_products(request):
    """List products"""
    products = list(Product.objects.values())

    return JsonResponse(products, safe=False)  # or JsonResponse({'data': data})


def dump_data(request):
    filename = "inventory_dumped_data.json"
    filepath = _create_db_json_file(filename)
    if os.path.exists(filepath):
        with open(filepath, "rb") as fh:
            response = HttpResponse(
                fh.read(), content_type="application/force-download"
            )
            response["Content-Disposition"] = "filename=%s" % filename
            return response
    raise Http404


def _create_db_json_file(filename):
    db_file = open(os.path.dirname(__file__) + "/{}".format(filename), "w")
    # change application_name with your django app which you want to get backup from it
    call_command("dumpdata", "inventory", stdout=db_file, indent=3)
    db_file.close()
    return os.path.dirname(__file__) + f"/{filename}"
