from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', name='catalog'),
    url(r'^monitors/', include('catalog.mon_urls')),
    url(r'^cpu/', include('catalog.cpu_urls')),
]