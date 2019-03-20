"""rrphone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from . import views
from django.conf.urls import handler404, handler500
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('eport/', views.eport),
    path('aport/', views.aport),
    path('wx/',views.wx),
    path('insert/', views.insert),
    path('movie', views.movie),
    path('vvs', views.vvs),
    path('snow', views.snow),
    # path('wx/',views.wx),
]
handler404 = views.pag_no_found
handler500 = views.pag_errow
