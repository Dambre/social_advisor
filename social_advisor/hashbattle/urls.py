"""
hashbattle URL Configuration
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

from battle_app import views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('battle_app.urls')),
]

if settings.DEBUG:
	urlpatterns += [
		url(r'^plate/', include('django_spaghetti.urls')),
	]

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()