from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.home),
    path("login/",views.login_user,name="login"),
    path('register/',views.register_page,name='register'),
    # path('activate/',views.activate_email,name='activate'),
]
