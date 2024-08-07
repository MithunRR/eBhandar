# Generated by Django 5.0 on 2024-01-07 12:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eBh_Cust', '0015_order'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='wishlist')),
                ('productName', models.CharField(max_length=40)),
                ('price', models.IntegerField()),
                ('mrp', models.IntegerField()),
                ('desc', models.TextField(max_length=1000)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eBh_Cust.category')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eBh_Cust.product')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eBh_Cust.subcategory')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
