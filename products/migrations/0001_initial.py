# Generated by Django 5.1.3 on 2024-11-28 04:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.PositiveIntegerField(default=0)),
                ('color', models.CharField(blank=True, choices=[('Red', 'Red'), ('Blue', 'Blue'), ('Green', 'Green'), ('Black', 'Black'), ('White', 'White'), ('Other', 'Other')], max_length=16, null=True)),
                ('size', models.CharField(blank=True, choices=[('36', 'EU 36'), ('37', 'EU 37'), ('38', 'EU 38'), ('39', 'EU 39'), ('40', 'EU 40'), ('41', 'EU 41'), ('42', 'EU 42'), ('43', 'EU 43'), ('44', 'EU 44'), ('45', 'EU 45'), ('46', 'EU 46'), ('47', 'EU 47')], max_length=3, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.category')),
            ],
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='in_baskets', to='products.product')),
            ],
        ),
    ]
