from django.contrib import admin
from django.urls import path
from . import views
from products.views import add_to_cart

urlpatterns = [
    path("",views.home),
    path("login/",views.login_user,name="login"),
    path('register/',views.register_page,name='register'),
    path("add-to-cart/<uid>/",add_to_cart,name="add_to_cart"),
    path("cart/",views.cart,name="cart"),
    # path('activate/',views.activate_email,name='activate'),
]
