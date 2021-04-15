from django.shortcuts import render,redirect
from mobile.forms import BrandCreateForm,MobileCreateForm,UserRegForm,OrderForm
from .models import Brands,Mobile,Orders

from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
# Create your views here.
def admin_permissipon_required(func):
    def wrapper(request):
        if not request.user.is_superuser:
            return redirect("errorpage")
        else:
            return func(request)
    return wrapper
def admin_permissipon_required2(func):
    def wrapper(request,id):
        if not request.user.is_superuser:
            return redirect("errorpage")
        else:
            return func(request,id)
    return wrapper
@admin_permissipon_required
def brand_view(request):

    brand=Brands.objects.all()
    forms=BrandCreateForm
    context={}
    context["brands"]=brand
    context["form"]=forms
    if request.method=="POST":
        form=BrandCreateForm(request.POST)
        if form.is_valid():
            form.save()
            print("Saved")
            return redirect("brandview")
    return render(request,"mobile/brandcreate.html",context)

def errorpg(request):
    return render(request,"mobile/errorpg.html")

@admin_permissipon_required2
def brand_del(request,id):
    brand=Brands.objects.get(id=id)
    brand.delete()
    return redirect("brandview")
@admin_permissipon_required2
def brand_update(request,id):
    brand = Brands.objects.get(id=id)
    form=BrandCreateForm(instance=brand)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=BrandCreateForm(request.POST,instance=brand)
        context["form"]=form
        if form.is_valid():
            form.save()
            return redirect("brandview")
    return render(request,"mobile/brandupd.html",context)
@admin_permissipon_required
def mobile_create(request):
    mobiles = Mobile.objects.all()
    form=MobileCreateForm
    context={}
    context["form"]=form
    context["mobiles"] = mobiles
    if request.method=="POST":
        form=MobileCreateForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            print("save")
            return redirect("mobcrt")
    return render(request,"mobile/mobilecreate.html",context)
@admin_permissipon_required2
def mobile_update(request,id):
    mobiles=Mobile.objects.get(id=id)
    form=MobileCreateForm(instance=mobiles)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=MobileCreateForm(request.POST,instance=mobiles,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("mobcrt")

    return render(request,"mobile/mobileupd.html",context)
@admin_permissipon_required2
def mobile_delete(request,id):
    mobiles=Mobile.objects.get(id=id)
    mobiles.delete()
    return redirect("mobcrt")
def list_mobiles(request):
    mobiles=Mobile.objects.all()
    context={}
    context["mobiles"]=mobiles
    return render(request,"mobile/listmobiles.html",context)
def mpbile_detail(request,id):
    mobile=Mobile.objects.get(id=id)
    context={}
    context["mobile"]=mobile
    return render(request,"mobile/mobiledetail.html",context)


def user_registration(request):
    form=UserRegForm
    context={}
    context["form"]=form
    if request.method=="POST":
        form=UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("userlog")
        else:
            form=UserRegForm(request.POST)
            context["form"]=form
            return render(request, "mobile/usereg.html", context)
    return render(request,"mobile/usereg.html",context)
def user_login(request):

    if request.method=="POST":
        username=request.POST.get("uname")
        password=request.POST.get("pswd")
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect("listmob")
        else:
            return render(request, "mobile/userlogin.html")
    return render(request,"mobile/userlogin.html")

def user_logout(request):
    logout(request)
    return redirect("userlog")



def order_details(request,pk):
    prodect=Mobile.objects.get(id=pk)

    form=OrderForm(initial={'user':request.user,'prodect':prodect})
    context={}
    context["form"]=form
    if request.method=="POST":
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            print("success")
            return redirect("crt")
        else:
            return redirect("orderdet")
    return render(request,"mobile/order.html",context)
def cart_details(request):
    order=Orders.objects.all()
    context={}
    context["orders"]=order
    return render(request,"mobile/Cart.html",context)