from django.shortcuts import render
from app.models import Products
from app.models import Addtocart
from app.models import Wishlist
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import logout as log_out
from django.db.models import Sum
from django.contrib.auth import login as as_login
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from app.models import Order
# Create your views here.
def index(request):
    # wish = Wishlist.objects.all().count()
    # cart = Addtocart.objects.all().count()
    # request.session['wishcount'] =wish
    # request.session['cartcount'] =cart
    prodname =Products.objects.filter(Product_Category="cata")
    prodname2 =Products.objects.filter(Product_Category="catb")
    x={'prodname':prodname,'prodname2':prodname2}
    return render(request,"pages/index.html",{'x':x})

def product(request, id):
    obj = Products.objects.get(pk=id)
    return render(request, 'pages/product.html', {'prod':obj})

def adddel(request,id):
    Addtocart.objects.filter(Product_id=id).delete()
    return redirect('cart')

def addcard(request,id):
    if request.user.is_authenticated:
        obj = Products.objects.get(pk=id)
        if Addtocart.objects.filter(Product_id=id).exists() :
            messages.success(request, 'Product Already Added in your Card!')
            return redirect('/')
        else:
            users=request.user.id
            Product_id=obj.id
            Product_name=obj.Product_name
            Product_Price=obj.Product_Price
            Product_Discount_price=obj.Product_Discount_price
            Product_Unit=obj.Product_Unit
            Product_img=obj.Product_img
            reg=Addtocart(user_id=users,Product_id=Product_id,Product_name=Product_name,Product_Price=Product_Price,Product_Discount_price=Product_Discount_price,Product_Unit=Product_Unit,Product_img=Product_img,)
            reg.save()
            wish = Wishlist.objects.all().count()
            cart = Addtocart.objects.all().count()
            request.session['wishcount'] =wish
            request.session['cartcount'] =cart
            messages.success(request, 'Product Succesfully Add in your Card!')
            return redirect('/')
    else:
        return redirect('login')
# ...................end add to cart.................................

def whishlist2(request,id):
    if request.user.is_authenticated:
        obj = Products.objects.get(pk=id)
        if Wishlist.objects.filter(Product_id=id).exists() :
            messages.success(request, 'Product Already Added in your Whislist!')
            return redirect('/')
        else:
            users=request.user.id
            Product_id=obj.id
            Product_name=obj.Product_name
            Product_Price=obj.Product_Price
            Product_Discount_price=obj.Product_Discount_price
            Product_Unit=obj.Product_Unit
            Product_img=obj.Product_img
            reg=Wishlist(user_id=users,Product_id=Product_id,Product_name=Product_name,Product_Price=Product_Price,Product_Discount_price=Product_Discount_price,Product_Unit=Product_Unit,Product_img=Product_img,)
            reg.save()
            wish = Wishlist.objects.all().count()
            cart = Addtocart.objects.all().count()
            request.session['wishcount'] =wish
            request.session['cartcount'] =cart
            messages.success(request, 'Product Succesfully Add in your Whislist!')
            return redirect('/')
    else:
        return redirect('login')


def cart(request):
    if request.user.is_authenticated:
        cart = Addtocart.objects.all()
        wish = Wishlist.objects.all().count()
        cart2 = Addtocart.objects.all().count()
        cartprice=Addtocart.objects.aggregate(Sum('Product_Discount_price'))
        cartpr=cartprice.get('Product_Discount_price__sum')
        totalgd=cartpr+40
        x={'cartprice':cartpr, 'cart':cart,'total':totalgd}
        request.session['wishcount'] =wish
        request.session['cartcount'] =cart2
        return render(request, 'pages/cart.html',{'cart':x})
    else:
       return redirect("login")

def wishlist(request):
    if request.user.is_authenticated:
        wish = Wishlist.objects.all()
        wish2 = Wishlist.objects.all().count()
        cart = Addtocart.objects.all().count()
        request.session['wishcount'] =wish2
        request.session['cartcount'] =cart
        return render(request, 'pages/wishlist.html', {'wish':wish})
    else:
        return redirect("login")

def wishdel(request,id):
    Wishlist.objects.filter(Product_id=id).delete()
    return redirect('wishlist')

def logout(request):
    del request.session['wishcount']
    del request.session['cartcount']
    Wishlist.objects.all().delete()
    Addtocart.objects.all().delete()
    log_out(request)
    return redirect('home')

def userlogin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        as_login(request, user)
        wish = Wishlist.objects.all().count()
        cart = Addtocart.objects.all().count()
        request.session['wishcount'] =wish
        request.session['cartcount'] =cart
        messages.success(request, 'Welcome to Celebration Process !')
        return redirect('/')
    else:
        messages.error(request, 'Please Fill valid User Name And Password')
        return redirect('login')


def login(request):
    return render(request, 'pages/login.html')

def register(request):
    return render(request, 'pages/register.html')

def regdata(request):
    try:
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if (password==cpassword):
            password2=make_password(password)
            reg=User(username=username,email=email,first_name=first_name,last_name=last_name,password=password2,)
            print(username)
            reg.save()
            messages.success(request, 'Your Are Successfully Registered!')
            return redirect('register')
        else:
            messages.error(request, 'Password and confirm password does not matched!')
            return redirect('register')
    except:
        messages.error(request, 'Please Try Again Something is Wrong')
        return redirect('register')
#                    end resitration

def checkout(request):
    cart2=Addtocart.objects.all()
    cartprice=Addtocart.objects.aggregate(Sum('Product_Discount_price'))
    cartpr=cartprice.get('Product_Discount_price__sum')
    totalgd=cartpr+40
    x={'cartprice':cartpr, 'cart':cart2,'total':totalgd}
    return render(request, 'pages/checkout.html',{'x':x})

def myacc(request):
    return render(request, 'pages/myaccount.html')

def shop(request):
    shop=Products.objects.all()
    return render(request, "pages/shop.html",{"shop":shop})

def order(request):
    userid = request.POST['userid']
    username = request.POST['username']
    email = request.POST['email']
    phone = request.POST['phone']
    address = request.POST['address']
    country = request.POST['country']
    city = request.POST['city']
    state = request.POST['state']
    zipcode = request.POST['zipcode']
    payment = request.POST['payment']
    print(payment)
    try:
        reg=Order(userid=userid,username=username,email=email,phone=phone,address=address,country=country,city=city,state=state,zipcode=zipcode,payment=payment,)
        reg.save()
        Wishlist.objects.all().delete()
        Addtocart.objects.all().delete()
        messages.error(request, 'Your Order Succesfully Placed')
        return redirect('/')

    except:
        messages.error(request, 'Please Try Again Something is Wrong')
        return redirect('checkout')

    return redirect('/')