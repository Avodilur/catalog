from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.category, name='catalog'),
    url(r'^(\D+)/[(\D+)/]*', views.category, name='category'),
]