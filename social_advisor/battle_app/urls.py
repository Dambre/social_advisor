from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^analyze/$', views.get_user_input, name='get_user_input'),
    url(r'^analyze/(?P<word>[-\w]+)/$', views.get_word_statistics),
]