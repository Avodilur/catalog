from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.catalog, name='catalog'),
    url(r'^(?P<category>\D+)/(?P<subcategory>\D+)/', views.subcategory, name='subcategory'),
    url(r'^(?P<category>\D+)/', views.category, name='category'),
]