# Generated by Django 4.0 on 2023-01-15 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0004_delete_customeraddress'),
        ('Ecomm', '0005_alter_orderitem_order_alter_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customer_addresses', to='Accounts.customer')),
            ],
        ),
    ]
