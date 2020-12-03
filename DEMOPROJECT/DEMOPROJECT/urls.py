"""DEMOPROJECT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, include

from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='base'),
    path('noti/', views.noti, name='noti'),
    # path('tlogin/', views.tlogin, name='tlogin'),
    # path('slogin/', views.slogin, name='slogin'),
    path('signup/', views.signup, name='signup'),
    # path('tlogin/', views.tlogin, name='tlogin'),
    path('login/', auth_views.LoginView.as_view(template_name='app1/login.html'), name='login'),
    path('slogin/', auth_views.LoginView.as_view(template_name='app1/slogin.html'), name='slogin'),
    path('tlogin/', auth_views.LoginView.as_view(template_name='app1/tlogin.html'), name='tlogin'),
    path('logout/', auth_views.LogoutView.as_view(template_name='app1/logout.html'), name='logout'),
    path('', include('app1.urls')),
]
