# Generated by Django 2.1.4 on 2019-01-09 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_server', '0011_product_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='amount',
        ),
    ]
