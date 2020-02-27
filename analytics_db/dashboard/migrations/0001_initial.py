# Generated by Django 3.0.3 on 2020-02-27 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('product_category', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('payment_method', models.CharField(max_length=50)),
                ('shipping_cost', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('datetime', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
