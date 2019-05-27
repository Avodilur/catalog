from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^(\D+)/product/(\d+)$', views.product),
    url(r'^(\S+)*', views.category, name='category'),
]
