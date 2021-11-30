"""SilviaOrsi URL Configuration

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
from django.urls import path
from Setup.views import welcome,login,logout
from Depilacion.views import reservas,reserva_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome),
    path('login/', login),
    path('logout/', logout),
    path('reservas/',reservas),
    path('reservas_list/',reserva_list),
]

admin.site.site_header ="Silvia Orsi"
admin.site.site_title ="Silvia Orsi"
