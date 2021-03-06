# Generated by Django 3.2.6 on 2021-08-24 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_management', '0002_profile_profile_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.BooleanField(default=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('stock_quantity', models.IntegerField()),
                ('min_order', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('max_order', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('pick_yourself', models.BooleanField(default=True)),
                ('additional_desc', models.CharField(blank=True, max_length=250)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.product')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user_management.profile')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.unit')),
            ],
        ),
    ]
