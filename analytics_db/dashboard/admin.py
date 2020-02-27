from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('product_category','datetime','payment_method','shipping_cost','price')
    search_fields = ['product_category']


admin.site.register(Order, OrderAdmin)
