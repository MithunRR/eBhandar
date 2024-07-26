from django.contrib import admin
from .models import Offer_Banner,Product, Category, Subcategory, InstaCart, RegulCart, Order, Wishlist

# Register your models here.
admin.site.register(Offer_Banner)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Subcategory)

admin.site.register(InstaCart)
admin.site.register(RegulCart)
admin.site.register(Order)
admin.site.register(Wishlist)





