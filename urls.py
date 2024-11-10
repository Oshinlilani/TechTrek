"""
URL configuration for minorProject project.

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
from minorProject import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin-panel/', views.homePage,name="home"),
    path('headphone/', views.headphone,name="headphone"),
    path('loginpage/', views.loginPage,name="loginpage"),
    path('smartwatch/', views.smartwatch,name="smartwatch"),
    path('register/', views.register,name="register"),
    path('order/', views.order,name="order"),
    path('earbud/', views.earbud,name="earbud"),
    

]
