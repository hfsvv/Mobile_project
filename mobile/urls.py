from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from .views import brand_view,brand_del,brand_update,mobile_create,list_mobiles,mpbile_detail,user_registration,user_login,user_logout,order_details,errorpg,cart_details,mobile_delete,mobile_update
urlpatterns = [
    path("mobiles/details/<int:id>",mpbile_detail,name="mdetail"),
    path("mobiles/order/<int:pk>",order_details,name="orderdet"),
    path("error",errorpg,name="errorpage"),
    path("",lambda request:render(request,"mobile/index.html")),
    path("brands",brand_view,name="brandview"),
    path("brands/del/<int:id>",brand_del,name="branddel"),
    path("brands/upd/<int:id>",brand_update,name="brandup"),
    path("mobiles",mobile_create,name="mobcrt"),
    path("mobiles/list",list_mobiles,name="listmob"),
    path("mobiles/userreg",user_registration,name="userreg"),
    path("mobiles/userlogin",user_login,name="userlog"),
    path("mobiles/userlogout",user_logout,name="ulogout"),
    path("mobiles/cart",cart_details,name="crt"),
    path("mobiles/del/<int:id>",mobile_delete,name="mobdel"),
    path("mobiles/upd/<int:id>",mobile_update,name="mobupd")

]
