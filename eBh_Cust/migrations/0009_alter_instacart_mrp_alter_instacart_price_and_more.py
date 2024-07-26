# Generated by Django 5.0 on 2024-01-07 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eBh_Cust', '0008_instacart_product_regulcart_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instacart',
            name='mrp',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='instacart',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='regulcart',
            name='mrp',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='regulcart',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]