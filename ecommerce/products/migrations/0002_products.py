# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-28 02:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('category', models.CharField(choices=[('Electronics', 'EL'), ('Clothing', 'CL'), ('Groceries', 'GR'), ('Accesories', 'AC'), ('Food and Beverages', 'FB')], default='EL', max_length=50)),
                ('exp_date', models.DateField()),
                ('reviews', models.CharField(max_length=255)),
                ('ratings', models.CharField(max_length=10)),
                ('return_policy', models.CharField(choices=[('Yes', 'Y'), ('No', 'N')], default='Y', max_length=5)),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='store_prod', to='products.Stores')),
            ],
        ),
    ]
