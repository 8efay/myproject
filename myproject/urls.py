"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from exercise import views

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', views.home, name='home'),  # Ev sayfası
  # Anasayfa
    path('about/', views.about, name='about'),  # Hakkımızda
    path('contact/', views.contact, name='contact'),  # İletişim
    path('boyun/',views.boyun,name='boyun'),
    path('omuz/',views.omuz,name='omuz'),
    path('sırt/',views.sırt,name='sırt'),
    path('bel/',views.bel,name='bel'),
    path('el_ve_el_bilegi/',views.el_ve_el_bilegi,name='el_ve_el_bilegi'),
    path('kalca/',views.kalca,name='kalca'),
    path('ayak/',views.ayak,name='ayak'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
