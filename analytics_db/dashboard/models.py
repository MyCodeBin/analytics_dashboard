from django.db import models


# Create your models here.
class Order(models.Model):
    product_category = models.CharField(max_length=50, primary_key=True)
    payment_method = models.CharField(max_length=50)
    shipping_cost = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    datetime = models.DateTimeField(auto_now=True, editable=True, null=True)

    def __str__(self):
        return self.product_category
