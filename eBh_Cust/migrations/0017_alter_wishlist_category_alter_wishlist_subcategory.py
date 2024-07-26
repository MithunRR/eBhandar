# Generated by Django 5.0 on 2024-01-07 13:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eBh_Cust', '0016_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='eBh_Cust.category'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='eBh_Cust.subcategory'),
        ),
    ]