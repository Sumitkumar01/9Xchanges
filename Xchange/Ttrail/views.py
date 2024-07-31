from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import *
# Create your views here.


def WelcomePage(request):
    return render(request,"Ttrail/index1.html")

def WelcomePage1(request):
    return render(request,"Ttrail/index.html")


def LoginPage(request):
    #2 This view will return when METHOD=="POST" -> login PROCEDURE
    if request.method=="POST":
        Email = request.POST['Email']                   #* Fetch Email from LOGIN form
        Password = request.POST['Password']             #* Fetch Password from LOGIN form

        user = authenticate(request, Email=Email, password=Password)    #* Verify Auth for user if valid or not
        if user is not None:
            login(request, user)                        #* LOGIN user if Credintials are found to be Correct
            return render(request,"Ttrail/index.html")  
        
        else:                                           #* IF Login Credintials are wrong..
            context={
                "message":"User Not Found!!!"
            }
            return render(request,"Ttrail/Auth/Login.html",context) #* Return To Login Page with FAILED message
        
    #1 This view will return when METHOD="GET" normal Login page.
    return render(request,"Ttrail/Auth/Login.html")



def RegisterPage(request):
    if request.method=="POST":
        First_Name = request.POST['first_name']
        Last_Name = request.POST['Last_name']
        Email = request.POST['Email']
        Password = request.POST['Password']
        Cpassword = request.POST['Confirm_Password']
        
        if Password==Cpassword:
            user = Admin.objects.create(Email=Email)
            user.set_password(Password)
            user.save()

            return render(request,"Ttrail/Auth/Login.html")
        else:
            context={
                "message":"Password and Confirm Password Should not be Same"
            }

            return render(request,"Ttrail/Auth/Register.html",context)
        

    return render(request,"Ttrail/Auth/Register.html")


def FaqPage(request):
    return render(request,"Ttrail/Faq.html")


def AboutPage(request):
    return render(request,"Ttrail/About.html")

def LocationPage(request):
    return render(request,"Ttrail/Location.html")

def WishlistPage(request):
    return render(request,"Ttrail/Wishlist.html")

def AddListingPage(request):
    return render(request,"Ttrail/AddListing.html")

def AccountPage(request):
    return render(request,"Ttrail/Account.html")

def ContactPage(request):
    return render(request,"Ttrail/Contact.html")


def BlogPage(request):
    return render(request,"Ttrail/Blog.html")


def BlogDetailPage(request):
    return render(request,"Ttrail/Blogdetail.html")
