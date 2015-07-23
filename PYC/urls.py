"""Planyourcity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
import core.views as coreviews
from django.contrib.auth import views as auth_views

urlpatterns = [
    	url(r'^admin/', include(admin.site.urls)),
        url(r'index/', coreviews.inicio),
        url(r'^$', 'core.views.home', name='home'),
        url(r'home/$', coreviews.home),
        url('', include('social.apps.django_app.urls', namespace='social')),
        url('', include('django.contrib.auth.urls', namespace='auth')),
    	url(r'listado/$', coreviews.lista_eventos_creados),
	    url(r'^detalle/(?P<titulo>.+)/$', coreviews.detalle),
        url(r'^ofertar/(?P<categoria>.+)/$', coreviews.ofertar),
        url(r'^buscar/(?P<categoria>.+)/(?P<page>[0-9]+)/$', coreviews.buscar),
        url(r'^buscar/(?P<categoria>.+)/$', coreviews.menu_buscar),
        url(r'^calendario', coreviews.calendario),
        url(r'^misactividades', coreviews.misactividades_seguidas),
        url(r'^all_events/', coreviews.all_events),
]


