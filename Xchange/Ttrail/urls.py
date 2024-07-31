from django.urls import path,include
from .views import *

urlpatterns = [
    path('',WelcomePage,name="Welcome"),
    path('welcome/',WelcomePage1,name="Welcome1"),
    path('Login/',LoginPage,name="Login"),
    path('Register/',RegisterPage,name="Register"),
    path('about/',AboutPage,name="About"),
    path('faq/',FaqPage,name="Faq"),
    path('location/',LocationPage,name="Location"),
    path('wishlist/',WishlistPage,name="Wishlist"),

    path('addlist/',AddListingPage,name="AddListing"),
    path('account/',AccountPage,name="Account"),
    path('contact/',ContactPage,name="Contact"),



    path('blog/',BlogPage,name="Blog"),
    path('blogdetail/',BlogDetailPage,name="BlogDetail")
]


