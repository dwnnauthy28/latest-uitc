from django.db import models
from django.contrib.auth.models import AbstractUser 
from datetime import datetime, date

from sqlalchemy import false



# Create your models here.

class Registration(AbstractUser):
    userType = [
            ('BORROWER','Borrower'),
            ('STAFF', 'Staff'),
    ]        
    idnumber = models.IntegerField(verbose_name='idNumber', unique=True)
    userType = models.CharField(max_length=30, choices= userType, verbose_name='userType', default= 'BORROWER')


class Inventory(models.Model):
    choices = [
        ('Available','Available'),
        ('Not Available', 'Not Available'),
    ]
    itemname = models.CharField(max_length=30, verbose_name='itemname')
    status = models.CharField(max_length=30, choices= choices, verbose_name='status', default='Available')

    
    def __str__(self):
        return self.itemname



class Borrowing(models.Model):
    choices = [
        ('Pending','Pending'),
        ('Approve', 'Approve'),
        ('Not Approve', 'Not Approve'),
        ('Return', 'Return'),
        
    ]
    idNumber = models.CharField(max_length=99,verbose_name='idNumber')
    itemname = models.CharField(max_length=99,verbose_name='itemname')    
    date_borrow = models.DateField(auto_now_add=True, verbose_name='date_borrow')
    date_return = models.DateField(auto_now_add=False, verbose_name='date_return')
    description = models.TextField(max_length= 150, verbose_name='description', null= True)
    status = models.CharField(max_length=30, choices= choices, verbose_name='status', default='Pending')
    
    def __str__(self):
        return self.idNumber


   

    

    
    


