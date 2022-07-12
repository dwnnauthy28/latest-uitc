from django.contrib import admin
from django.urls import path
from django.urls.conf import include


from . import views

urlpatterns = [
    path('', views.userpage, name="userpage"),
    path('loginborrower/', views.loginborrower, name= "loginborrower"),
    path('registration/', views.registration, name= "registration"),
    path('registration2/', views.registration2, name= "registration2"),
    path('loginstaff/', views.loginstaff, name= "loginstaff"),
    path ('logout/', views.logoutuser, name = 'logout'),
    path('dashboard/', views.dashboard, name= "dashboard"),
    path('dashstud/', views.dashstud, name= "dashstud"),
    path('inventory/', views.inventory, name= "inventory"),
    path('inventoryadd/', views.inventoryadd, name= "inventoryadd"),
    path('update/<int:pk>', views.update, name = "update" ),
    path('delete/<int:pk>', views.delete, name = "delete" ),
    path('borrowing/', views.borrowing, name= "borrowing"),
    path('borrowingform/<int:pk>', views.borrowingform, name= "borrowingform"),
    path('borrowstatus/', views.borrowstatus, name= "borrowstatus"),
    path('borrowreturn/<int:pk>', views.borrowreturn, name = "borrowreturn" ),
    path('summary/', views.summary, name= "summary"),
    path('summaryupdate/<str:pk>', views.summaryupdate, name = "summaryupdate" ),
    path('pdf_gen/', views.pdf_gen, name = "pdf_gen" )
    #path('updatestatus/<int:pk>', views.updatestatus, name= "updatestatus"),
    #path('Adding/', views.Adding, name = "Adding" ),
]