# Generated by Django 5.0 on 2024-01-06 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eBh_Cust', '0003_instacart_user_regulcart_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instacart',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
