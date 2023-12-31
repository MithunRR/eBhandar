from django.shortcuts import render
from .models import Offer_Banner

# Create your views here.
def index(request):
    offer_banner = Offer_Banner.objects.all()
    return render(request, 'index.html', {'o_f': offer_banner})

def about(request):
    return render(request, 'about.html')

def cart(request):
    return render(request, 'cart.html')

def account(request):
    return render(request, 'account.html')

def profile(request):
    return render(request, 'profile.html')

def address(request):
    return render(request, 'addresses.html')

def checkout(request):
    return render(request, 'checkout.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def productView(request):
    return render(request, 'productView.html')

def search_n_cat(request):
    return render(request, 'search_n_cat.html')