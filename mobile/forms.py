from django.forms import ModelForm,forms
from django import forms
from mobile.models import Brands,Mobile,Orders
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BrandCreateForm(ModelForm):
    class Meta:
        model=Brands
        fields="__all__"
class MobileCreateForm(ModelForm):
    class Meta:
        model=Mobile
        fields="__all__"

class UserRegForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2']

class OrderForm(ModelForm):
    # prodect=forms.CharField(max_length=150)
    class Meta:
        model=Orders
        fields='__all__'

# class CartForm(ModelForm):
#     prodect=forms.CharField(max_length=150)
#     class Meta:
#         model=Orders
#         fields=['prodect','user','status']

