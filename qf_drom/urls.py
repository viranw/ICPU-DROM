"""qf_drom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from . import views as baseViews
from users import views as userViews
from flights import views as flightViews

urlpatterns = [
    path('database/', admin.site.urls),
    path('login/', userViews.login, name="login"),
    path('logout/', userViews.logout, name="logout"),

    path('', baseViews.start, name='start'),

    path('flights/<int:flight_id>/admin/', include('flights.urls_admin')),
    path('flights/<int:flight_id>/', include('flights.urls_public')),


    path('passenger/<str:url_key>', flightViews.passenger_page, name="passenger"),

]
