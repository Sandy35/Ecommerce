# Generated by Django 4.0 on 2023-01-15 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_customeraddress'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomerAddress',
        ),
    ]