# Generated by Django 3.1.5 on 2022-05-05 07:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'brand',
                'verbose_name_plural': 'brands',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False)),
                ('transaction_id', models.CharField(default=None, max_length=200, null=True)),
                ('customer', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_of_customer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'orders',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('qty', models.IntegerField()),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.FileField(upload_to='uploads/products/')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_brand', to='store.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_category', to='store.category')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=None, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_item', to='store.order')),
                ('product', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_item', to='store.product')),
            ],
            options={
                'verbose_name': 'order_item',
                'verbose_name_plural': 'order_items',
            },
        ),
    ]
