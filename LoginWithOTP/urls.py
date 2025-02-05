"""
URL configuration for LoginWithOTP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.LandingPage,name='homepage'),
    path('login/',views.loginPage,name='login'),
    path('register/',views.RegisterPage,name='register'),
    path('logout/',views.logouted,name='logout'),
    path('ottp/',views.ottp,name="ottp"),
    path('forget/',views.forgetpass,name='forgetpass'),
    path('reset/',views.reset,name='reset'),
]
