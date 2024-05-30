"""
URL configuration for Weather_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from weather.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", day),
    path("day1", day1),
    path("day2", day2),
    path("day3", day2),
    path("day4", day2),
    path("day5", day2),
    path("day6", day2),
    path("weather", weather_view)
]
