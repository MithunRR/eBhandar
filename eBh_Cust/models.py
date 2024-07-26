from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Offer_Banner(models.Model):
    img = models.ImageField(upload_to='offer_banners')


class Category(models.Model):
    category = models.CharField(max_length=50)   
    def __str__(self):
        return self.category
    
class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    subcategory = models.CharField(max_length=50)   
    def __str__(self):
        return self.subcategory    

class Product(models.Model):
    productName = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    price = models.IntegerField(default=100)
    mrp = models.IntegerField(default=100)
    weight = models.CharField(max_length=10)
    desc = models.TextField(max_length=1000)

    img = models.ImageField(upload_to='all_prods')
    img2 = models.ImageField(upload_to='all_prods')
    img3 = models.ImageField(upload_to='all_prods')
    img4 = models.ImageField(upload_to='all_prods')
    img5 = models.ImageField(upload_to='all_prods')
    img6 = models.ImageField(upload_to='all_prods')    

    def __str__(self):
        return f'{self.productName} | {self.weight}' 
    
class InstaCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    img = models.ImageField()
    productName = models.CharField(max_length=40)
    price = models.IntegerField()
    mrp = models.IntegerField()
    quantity = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.IntegerField()
    def __str__(self):
        return f'{self.user} | {self.quantity} x {self.productName}'

class RegulCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    img = models.ImageField()
    productName = models.CharField(max_length=40)
    price = models.IntegerField()
    mrp = models.IntegerField()
    quantity = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.IntegerField()
    def __str__(self):
        return f'{self.user} | {self.quantity} x {self.productName}'
    

class Order(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    productName = models.CharField(max_length=40)
    price = models.IntegerField()
    mrp = models.IntegerField()
    quantity = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
 
    def __str__(self):
        return f'{self.user} | {self.quantity} x {self.productName} | {self.order_date}'
    
class Wishlist(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='wishlist') 
    productName = models.CharField(max_length=40)
    price = models.IntegerField()
    mrp = models.IntegerField()
    desc = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

