# Generated by Django 3.2.6 on 2021-08-21 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_type',
            field=models.CharField(choices=[('producer', 'Producer'), ('customer', 'Customer')], default='customer', max_length=8),
        ),
    ]
