# Generated by Django 3.2.6 on 2021-08-11 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliverylocation',
            name='phone',
            field=models.CharField(max_length=12),
        ),
    ]
