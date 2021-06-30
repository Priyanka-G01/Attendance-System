"""Attendance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
import employee.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome', employee.views.welcome,name="welcome"),
    path('showdata', employee.views.showdata),
    path('Adddata', employee.views.Adddata),
    path('load_form'  , employee.views.load_form),
    path('add' , employee.views.add),
    path('show',employee.views.show),
    path('edit/<int:id>',employee.views.edit),
    path('update/<int:id>',employee.views.update),
    path('delete/<int:id>',employee.views.delete),
    path('search',employee.views.search),
    path('load_attendance',employee.views.load_attendance),
    path('add_att',employee.views.add_att),
    path('show_att',employee.views.show_att),
    path('delete_att/<int:id>',employee.views.delete_att),
    path('edit_att/<int:id>',employee.views.edit_att),
    path('change/<int:id>',employee.views.change),
    path('register',employee.views.register,name="register"),
    path('employee/',include('django.contrib.auth.urls')),
    path('today',employee.views.today),
    ]


