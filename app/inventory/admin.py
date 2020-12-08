from django.contrib import admin
from inventory.models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    # All fields by default
    # pass
    # Custom fields
    # fields=["name", "price", "stock", "sku"]
    # Custom fieldsets
    list_display = ("name", "price", "stock", "calculate_income")
    fieldsets = [
        ("Required", {"fields": ["name", "price", "stock"]}),
        ("Optional", {"fields": ["description", "sku"]}),
    ]

    # Show a field after some data process
    def calculate_income(self, obj):
        return "$%.2f" % (obj.price * obj.stock)

    # Give it an short description to processed field
    calculate_income.short_description = "Possible income"


admin.site.register(Product, ProductAdmin)
