from django.contrib import admin
from .models import Product, ProductType


class ProductInline(admin.TabularInline):
    model = Product


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name', 'product_type', 'price']


class ProductTypeAdmin(admin.ModelAdmin):
    model = ProductType
    inlines = [ProductInline,]


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
