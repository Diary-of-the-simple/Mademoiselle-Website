from django.contrib import admin
from products.models import Product, Category, Collection, ProductVariation

# Register your models here.

admin.site.register(Category)
admin.site.register(Collection)
admin.site.register(Product)
admin.site.register(ProductVariation)