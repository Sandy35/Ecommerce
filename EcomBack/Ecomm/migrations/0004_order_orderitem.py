# Generated by Django 4.0 on 2023-01-15 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_remove_customer_email_remove_seller_email_and_more'),
        ('Ecomm', '0003_product_category_product_vendor_delete_vendor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_time', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.customer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ecomm.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ecomm.product')),
            ],
        ),
    ]
