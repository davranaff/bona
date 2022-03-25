from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
import datetime
from django.http import *
from django.db.models import Q
from django.core.mail import send_mail
# Create your views here.


def home_page(request):
    search = request.GET.get('search')
    product = Product.objects.all()
    category = Category.objects.all()
    result = None
    products = None
    if search:
        products = product.filter(Q(name__icontains=search))
        category = category.filter(Q(name__icontains=search))
        if product or category: result = True
    slider = Slider.objects.all()
    return render(request, 'home_page.html', {
        'product':product,
        'products':products,
        'slider':slider,
        'category':category,
        'result':result,
        'search':search
    })

def category_detail(request,pk):
    categorys = Category.objects.get(pk=pk)
    return render(request, 'category-detail.html', {'category':categorys})

# cart create

def add_to_cart(request,pk):
    kol = float(request.GET.get('kol'))
    if kol > 0:
        product = Product.objects.get(pk=pk)
        basket = Basket.objects.filter(owner=request.user, product=product)
        for item in basket:
            if item.product == product:
                item.quantity = kol
                item.save()
                return redirect('bonaapp:cart_url')
        Basket.objects.create(owner=request.user, product=product, quantity=kol)
        return redirect('bonaapp:cart_url')
    else:
        return HttpResponse('error')
# delete cart item

def delete_cart_item(request):
    basket_pk = request.GET.get('basket_pk')
    buylater_pk = request.GET.get('buylater_pk')
    if buylater_pk:
        buylater = BuyLater.objects.get(pk=buylater_pk)
        buylater.delete()
        return redirect('bonaapp:cart_url')
    if basket_pk:
        basket = Basket.objects.get(pk=basket_pk)
        basket.delete()
        return redirect('bonaapp:cart_url')

def cart(request):
    date_now = datetime.date.today()
    cart = Basket.objects.filter(owner=request.user)
    cart_later = BuyLater.objects.filter(owner=request.user)
    return render(request, 'cart.html', {'cart':cart,'date_now':date_now,'cart_later':cart_later})

def product_detail(request,pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product_detail.html', {'product':product})

def create_order(request):
    basket = Basket.objects.filter(owner=request.user)
    amount = sum([item.quantity for item in basket])
    total = sum([item.total_price() for item in basket])
    address = request.POST.get('address')
    email = request.POST.get('email')
    telephone_number = request.POST.get('telephone_number')

    if address and email and telephone_number:
        order = Order.objects.create(
            address=address,
            email=email,
            telephone_number=telephone_number,
            owner=request.user,
            buy=True,
            date = datetime.datetime.now()
        )
        if order.buy:
            x = None
            for item in basket:
                x = OrderProduct.objects.create(
                    order=order,
                    product=item.product,
                    amount=amount,
                    total=total,
                )
            basket.delete()
            messages.success(request,'success')
            return redirect('bonaapp:history_order_url')
    return render(request,'order.html',{'basket':basket, 'amount':amount,'total':total})

def history_order(request):
    order = Order.objects.filter(owner=request.user)
    return render(request,'history_order.html',{'order':order})


def buylater(request,pk):
    date = request.GET.get('date')
    if date:
        basket = Basket.objects.get(pk=pk)
        BuyLater.objects.create(
            owner = request.user,
            date = date,
            product = basket.product,
            quantity = basket.quantity,

        )
        basket.delete()
        messages.success(request,'Buy Later')
        return redirect('bonaapp:cart_url')


def buynow(request,pk):
    now = BuyLater.objects.get(pk=pk)
    Basket.objects.create(
        owner = request.user,
        product = now.product,
        quantity = now.quantity,
    )
    now.delete()
    return redirect('bonaapp:cart_url')


def return_order(request,pk):
    pass