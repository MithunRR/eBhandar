from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from .models import Offer_Banner, Product, Category, Subcategory, InstaCart, RegulCart, Order, Wishlist
from django.contrib.auth.models import User
from django.contrib import auth 
from django.db.models import Q
import json

# for base file
def get_subcategory(request):
    id = request.GET.get('id', '')
    result = list(Subcategory.objects.filter(category_id=int(id)).values('id', 'name'))
    return HttpResponse(json.dumps(result), content_type="application/json")

# Create your views here.
def index(request):
    offer_banner = Offer_Banner.objects.all()

    product = Product.objects.all()

    return render(request, 'index.html', {'o_f': offer_banner, 'product':product})

def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'index.html', {'product': product})

@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    if product.category.category in ['Fruit', 'Vegetable', 'Food']:
        quantity = 1
        price = product.price
        total = quantity * price
        cart_item = InstaCart.objects.create(
            product=product,
            user=request.user,
            quantity=quantity,
            productName=product.productName,
            price=price,
            mrp=product.mrp,
            img= product.img,
            total= price * quantity
        )
        print(total)
        cart_item.save()
        return redirect("/", {'total': total})
    else:
        quantity = 1 
        price = product.price
        total = quantity * price
        cart_item = RegulCart.objects.create(
            product=product,
            user=request.user,
            quantity=quantity,
            productName=product.productName,
            price=price,
            mrp=product.mrp,
            img= product.img,
            total= price * quantity
        )
        print(total)
        cart_item.save()
        return redirect("/", {'total': total})

@login_required
def remove_from_cart(request, item_id, product_id=None):
    try:
        if product_id is not None:
            # If both item_id and product_id are provided
            cart_item = InstaCart.objects.get(id=item_id)
            cart_item.delete()
            product = Product.objects.get(id=product_id)
            wishlist = Wishlist.objects.create(
                product=product,
                img=product.img,
                productName=product.productName,
                price=product.price,
                mrp=product.mrp,
                desc=product.desc,
                user=request.user
            )
        else:
            # If only item_id is provided
            cart_item = InstaCart.objects.get(id=item_id)
            cart_item.delete()
    except InstaCart.DoesNotExist:
        if product_id is not None:
            # If both item_id and product_id are provided
            cart_item = RegulCart.objects.get(id=item_id)
            cart_item.delete()
            product = Product.objects.get(id=product_id)
            wishlist = Wishlist.objects.create(
                product=product,
                img=product.img,
                productName=product.productName,
                price=product.price,
                mrp=product.mrp,
                desc=product.desc,
                user=request.user
            )
        else:
            # If only item_id is provided
            cart_item = RegulCart.objects.get(id=item_id)
            cart_item.delete()

    return redirect('/view_cart')

def wishlist(request):
    wishlist = Wishlist.objects.filter(user=request.user.id)
    return render(request, 'wishlist.html', {'wishlist':wishlist})

def search(request):
    search_query = request.GET.get('search', '')
    products = Product.objects.all()
    if search_query == "":
        n_pr = products.count()
    if search_query:
        product_name_results = Product.objects.filter(productName__icontains=search_query)
        desc_results = Product.objects.filter(desc__icontains=search_query)
        category_results = Product.objects.filter( Q(category__category__icontains=search_query) )
        products = product_name_results | desc_results | category_results
        n_pr = products.count()
    return render(request, 'search_n_cat.html', {'search_query': search_query, 'products':products, 'n_pr':n_pr }) 


def category(request, prcat):
    category = Category.objects.get(category=prcat)
    products = Product.objects.filter(category=category)
    return render (request, 'cat.html', {'products':products, 'category':category})

def view_cart(request):
    insta_cart_items = InstaCart.objects.filter(user=request.user.id)
    regul_cart_items = RegulCart.objects.filter(user=request.user.id)

    return render(request, 'cart.html', {'insta_cart': insta_cart_items, 'regul_cart': regul_cart_items})

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
    insta_cart_items = InstaCart.objects.filter(user=request.user.id)
    regul_cart_items = RegulCart.objects.filter(user=request.user.id)
    order = Order.objects.create(product=insta_cart_items)
    # order.productName = 
    return render(request, 'checkout.html', {'insta_cart': insta_cart_items, 'regul_cart': regul_cart_items})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)  
        if user is not None:
            auth.login(request, user)
            return redirect('/')     
        else:
            return redirect('/login') 
        
    else:    
        return render(request, 'login.html')
    
def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('/')
    

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            user = User.objects.create_user(username=username,first_name=first_name, last_name=last_name, email=email, password=password)
            user.save()
            return redirect('login')
        else:
            return redirect('signup')
    else:
        return render(request, 'signup.html')   
        

def productView(request, myid):
    product = Product.objects.filter(id=myid)
    return render(request, 'productView.html', {'product':product[0]})


def search_n_cat(request):
    return render(request, 'search_n_cat.html')