from audioop import add
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.urls import is_valid_path
from grpc import Status
from matplotlib.pyplot import get
from matplotlib.style import context
from numpy import save
from pyrsistent import v
from requests import post
from sqlalchemy import all_

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

from .forms import *
from .models import *

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, EmailMessage




# Create your views here.
def registration(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            name = request.POST ['first_name'] + "" + request.POST ['last_name']
            em = request.POST['email']
            message = 'You are succesfully registered in UITC Borrower, you can now borrow any equipment available in UITC.'
            mssg=EmailMessage(
                name,
                message,
                'groupuitc@gmail.com',
                [em], )

            mssg.send()
            return redirect('userpage')
        else:
            print(form.errors)
            

    context = {'form':form}

    return render (request, 'html/registration.html', context)

def registration2(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            name = request.POST ['first_name'] + "" + request.POST ['last_name']
            em = request.POST['email']
            message = 'You are succesfully registered in UITC Borrower,Kindly ask the admin to make you a staff member.'
            mssg=EmailMessage(
                name,
                message,
                'groupuitc@gmail.com',
                [em], )

            mssg.send()
            return redirect('userpage')
        else:
            print(form.errors)
            

    context = {'form':form}

    return render (request, 'html/registration.html', context)



def userpage(request):
    return render(request, 'html/userpage.html')

def logoutuser(request):
    logout(request)
    return redirect('userpage')

def loginborrower(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None and user.userType == 'BORROWER':
            login(request, user)
            return redirect('dashstud')
        else:
            messages.info(request, 'Username OR password is incorrect')
    return render(request, 'html/loginborrower.html',)


def loginstaff(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None and user.userType == 'STAFF':
            login(request, user)    
            return redirect('dashboard')
        else:
            messages.info(request, 'Username OR password is incorrect')
    return render(request, 'html/loginstaff.html',)

@login_required(login_url='loginstaff')
def dashboard(request):
    if request.user.is_authenticated and request.user.userType == 'STAFF':
        data = Borrowing.objects.all()
        context = {
            'data': data
        }
        print (context)
        return render(request, 'html/dashboard.html',context)
    return redirect ('loginstaff')


@login_required(login_url='loginborrower')
def dashstud(request):  
    if request.user.is_authenticated and request.user.userType == 'BORROWER':
        data = Inventory.objects.all()
        context = {
            'data': data
        }
        print (context)
        return render(request, 'html/dashboard-student.html',context)
    return redirect ('loginborrower')


@login_required(login_url='loginborrower')
def borrowing(request):
    if request.user.is_authenticated and request.user.userType == 'BORROWER':
        data = Inventory.objects.filter(status = 'Available')
        context = {
            
            'data': data
        }
        print (context)
        return render(request, 'html/borrowing.html',context)
    return redirect ('loginborrower')


@login_required(login_url='loginborrower')
def borrowingform(request,pk):
    if request.user.is_authenticated and request.user.userType == 'BORROWER':
        item = Inventory.objects.filter(id=pk).values('itemname')
        item2 = Inventory.objects.filter(id=pk).update(status = 'Not Available')
        req=request.user.idnumber
        if request.method == 'POST':
            item2 = Inventory.objects.filter(id=pk).update(status = 'Not Available')
            borrow = request.POST.get('borrow_item')
            print(borrow)
            id_numbers = request.POST.get('id_number')
            date_return = request.POST.get('date_return')   
            description = request.POST.get('description')
            data = Borrowing.objects.create(itemname= borrow, date_return = date_return,
                                            description = description, idNumber = req) 
            data.save()

            return redirect('borrowing')
        return render(request, 'html/borrowingform.html',{'itemname':item, 'idnumber':req} )
    else:
        return redirect('loginborrower') 




@login_required(login_url='loginborrower')
def borrowstatus(request):
    if request.user.is_authenticated and request.user.userType == 'BORROWER':
        data = Borrowing.objects.filter(status = 'Approve')
        context = {'data': data}
        print (context)
        return render(request, 'html/Borrowstatus (1).html',context)    
    return redirect ('loginborrower')

@login_required(login_url='loginborrower')
def borrowreturn(request,pk):
    if request.user.is_authenticated and request.user.userType == 'BORROWER':
        rtn = Borrowing.objects.filter(id=pk).update(status = 'Return')
        data = Borrowing.objects.get(id=pk)
        form = Borrowingform(instance=data)
    
    if request.method == "POST":
        form = Borrowingform(request.POST, instance=data)
        if form.is_valid():
            form.save()
        return redirect('borrowstatus')
    context = {'form': form}
    return render(request, 'html/borrowreturn.html', context )



@login_required(login_url='loginstaff')
def inventory(request):
    if request.user.is_authenticated and request.user.userType == 'STAFF':
        data = Inventory.objects.all()
        context = {
            'data': data
        }
        print (context)
        return render(request, 'html/inventory.html',context)
    return redirect ('loginstaff')


@login_required(login_url='loginstaff')
def inventoryadd(request):
    if request.user.is_authenticated and request.user.userType == 'STAFF':
        if request.method == 'POST':
            itemname = request.POST.get('itemname')
            print(itemname)
            newItem = Inventory.objects.create(itemname=itemname)
            newItem.save()
            return redirect('inventory')    
        return render(request, 'html/inventoryadd.html')
    return redirect('loginstaff') 

@login_required(login_url='loginstaff')
def update(request,pk):
    data = Inventory.objects.get(id=pk)
    form = Inventoryform(instance=data)
    
    if request.method == "POST":
        form = Inventoryform(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('inventory')
    context = {'form': form}
    return render(request, 'html/update.html', context)


@login_required(login_url='loginstaff')
def delete(request, pk):
	data = Inventory.objects.get(id=pk) 
	if request.method == "POST":
		data.delete()
		return redirect('inventory')
	context = {'itemname':data}
	return render(request, 'html/delete.html', context)
    


@login_required(login_url='loginstaff')
def summary(request):
    if request.user.is_authenticated and request.user.userType == 'STAFF':
        data = Borrowing.objects.filter(status = 'Pending')
        #data = Borrowing.objects.filter(status = 'Return')
        context = {'data': data}
        print (context)
        return render(request, 'html/summary.html',context)
    return redirect ('loginstaff')

@login_required(login_url='loginstaff')
def summaryupdate(request,pk):
    if request.user.is_authenticated and request.user.userType == 'STAFF':
        data = Borrowing.objects.get(id = pk)
        form = Borrowingform(instance=data)
        
        
        if request.method == "POST":
            form = Borrowingform(request.POST, instance=data)
            if form.is_valid():
                form.save()
                return redirect('summary')

        context = {'form': form}
    return render(request, 'html/summaryupdate.html', context )


@login_required(login_url='loginstaff')
def updatestatus(request,pk):
    if request.user.is_authenticated and request.user.userType == 'STAFF':
        data = Borrowing.objects.get(id=pk)
        form = Borrowingform(instance=data)
        item = Inventory.objects.filter(id=pk).values('itemname')
        
        if request.method == "POST":
            form = Borrowingform(request.POST, instance=data)
            if form.is_valid():
                form.save()
                return redirect('borrowstatus')
        context = {'form': form}
    return render(request, 'html/updatestatus.html', context, item)


def pdf_gen(request):
    data = Borrowing.objects.all()
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter ,bottomup=0)
    
    tob =c.beginText()
    tob.setTextOrigin(inch,inch)
    tob.setFont("Helvetica", 10)
    lines = []
            
    for val in data:
        lines.append(f'{val.date_borrow}'),
        lines.append(f'{val.date_return}'),
        lines.append(f'{val.idNumber}'),
        lines.append(f'{val.itemname}'),
        lines.append(f'{val.status}')
        lines.append('====================')
    for line in lines:
        tob.textLine(line)
    
    c.drawText(tob)
    c.showPage()
    c.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename = 'dashboard.pdf')


    


'''
def dell(request):
    return render(request,'html/delete.html')

def updatepage(request,id):  
    return render(request, 'html/updatepage.html', {'data': data})

def update(request,pk):
    update = add.objects.get(id=pk)
    form = Inventoryform(instance=update)
    return render(request,'html/update.html')

def Adding(request):
    

def delete(request, pk):
	eq = Add.objects.get(id=pk)
	if request.method == "POST":
		eq.delete()
		return redirect('delete')

	context = {'name':eq}
	return render(request, 'html/delete.html', context)
'''
