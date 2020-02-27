from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('product_category','datetime')
    search_fields = ['price']


admin.site.register(Order, OrderAdmin)
