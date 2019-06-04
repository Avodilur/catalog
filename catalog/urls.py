from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^search/$', views.search, name='search'),
    url(r'^(\D+)/product/(\d+)$', views.product),
    url(r'^(\S+)*', views.category, name='category'),
]
