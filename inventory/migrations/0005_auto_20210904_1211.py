# Generated by Django 3.2.6 on 2021-09-04 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20210825_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='additional_desc',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]
