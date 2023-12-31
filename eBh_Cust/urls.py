
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('cart', views.cart, name='cart'),
    path('account', views.account, name='account'),
    path('profile', views.profile, name='profile'),
    path('address', views.address, name='address'),
    path('checkout', views.checkout, name='checkout'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('productView', views.productView, name='productView'),
    path('search_n_cat', views.search_n_cat, name='search_n_cat'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)