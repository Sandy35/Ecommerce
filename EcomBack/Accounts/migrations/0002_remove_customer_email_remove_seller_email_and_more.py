# Generated by Django 4.0 on 2023-01-14 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='email',
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]