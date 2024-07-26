
from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^getSubcategory/$', views.get_subcategory),

    path('', views.index, name='index'),
    path('products/<int:pk>', views.product, name='product'),
    path('category/<str:prcat>', views.category, name='category'),

    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

    path('remove_from_cart/<int:item_id>/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),

    path('view_cart/', views.view_cart, name='ViewCart'),
    path('about', views.about, name='about'),
    path('account', views.account, name='account'),
    path('profile', views.profile, name='profile'),
    path('address', views.address, name='address'),
    path('checkout', views.checkout, name='checkout'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),

    path('product/<int:myid>/', views.productView, name='productView'),
    path('search/', views.search, name='search'),
    path('wishlist/', views.wishlist, name='wishlist'),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)