"""
hashbattle URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin

from battle_app import views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('battle_app.urls')),
]

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()