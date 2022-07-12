from cProfile import label
from multiprocessing.sharedctypes import Value
from pickle import READONLY_BUFFER
from pyexpat import model
from turtle import update
from attr import attr
from django import forms
from django.forms import DateField, ModelForm

from django.contrib.auth.models import User
from matplotlib import widgets
from nbformat import read
from pandas import value_counts

from .models import Inventory
from .models import Registration
from .models import Borrowing
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime






class CreateUserForm(UserCreationForm):
    class Meta:
        model = Registration
        fields = ['first_name','last_name','username','idnumber','email','password1','password2']
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control rounded-pill form-control-lg', 'placeholder':'Firstname'}),
            'last_name':forms.TextInput(attrs={'class':'form-control rounded-pill form-control-lg','placeholder':'Surname'}),
            'username':forms.TextInput(attrs={'class':'form-control rounded-pill form-control-lg','placeholder':'Username'}),
            'idnumber':forms.TextInput(attrs={'class':'form-control rounded-pill form-control-lg','placeholder':'Id Number'}),                                                                                                                                                      
            'email':forms.EmailInput(attrs={'class':'form-control rounded-pill form-control-lgl','placeholder':'Email'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control rounded-pill form-control-lg','placeholder':'Password'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control rounded-pill form-control-lg','placeholder':'Confirm Password'}),}
class ReceiverForm(UserCreationForm):
    class Meta:
        model = Registration
        fields = ['first_name','last_name','username','idnumber','email','password1','password2','userType']
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control rounded-pill form-control-lg', 'placeholder':'Firstname'}),
            'last_name':forms.TextInput(attrs={'class':'form-control rounded-pill form-control-lg','placeholder':'Surname'}),
            'username':forms.TextInput(attrs={'class':'form-control rounded-pill form-control-lg','placeholder':'Username'}),
            'idnumber':forms.TextInput(attrs={'class':'form-control rounded-pill form-control-lg','placeholder':'Id Number'}),                                                                                                                                                      
            'email':forms.EmailInput(attrs={'class':'form-control rounded-pill form-control-lgl','placeholder':'Email'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control rounded-pill form-control-lg','placeholder':'Password'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control rounded-pill form-control-lg','placeholder':'Confirm Password'}),
            }



'''
class Registrationform(ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'
        labels ={
            'fname':'',
            'sname':'',
            'inum':'',
            'email':'',
            'ps':'',
            'ps2':'',
        }
        widgets = {
            'fname':forms.TextInput(attrs={'class':'form-control rounded-pill form-control-lg', 'placeholder':'Firstname'}),
            'sname':forms.TextInput(attrs={'class':'form-control rounded-pill form-control-lg','placeholder':'Surname'}),
            'inum':forms.TextInput(attrs={'class':'form-control rounded-pill form-control-lg','placeholder':'ID Number'}),
            'email':forms.EmailInput(attrs={'class':'form-control rounded-pill form-control-lgl','placeholder':'Email'}),
            'ps':forms.PasswordInput(attrs={'class':'form-control rounded-pill form-control-lg','placeholder':'Password'}),
            'ps2':forms.PasswordInput(attrs={'class':'form-control rounded-pill form-control-lg','placeholder':'Confirm Password'}),
            }
'''

class Inventoryform(ModelForm):
    class Meta:
        model = Inventory
        fields = ['itemname','status']
        widgets = {
            'itemname':forms.TextInput(attrs={'class':'form-control rounded-pill form-control-lg', 'placeholder':'itemname'}),
            }
        
class Borrowingform(ModelForm):
    class Meta:
        model = Borrowing
        fields = ['itemname','description','date_return','status']
        widgets = {
            'itemname':forms.TextInput(attrs={'class':'form-control rounded-pill form-control-lg', 'placeholder':'itemname'}),
            'description':forms.TextInput(attrs={'class':'form-control rounded-pill form-control-lg', 'placeholder':'description'}),            
            
            }
