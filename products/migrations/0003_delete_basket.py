# Generated by Django 5.1.3 on 2024-11-28 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_created_at_alter_basket_added_at'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Basket',
        ),
    ]
