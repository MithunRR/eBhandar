from django.db import models

# Create your models here.

class Offer_Banner(models.Model):
    img = models.ImageField(upload_to='offer_banners')

class OrderInsp(models.Model):
    img = models.ImageField(upload_to='order_insp')
    productName = models.CharField(max_length=40)