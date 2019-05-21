from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.catalog, name='catalog'),
    # url(r'^[(?p<category>\D+)/]+$', views.category, name='category'),
    url(r'^(\D+)/[(\D+)/]*', views.category, name='category'),
    # url(r'^((?P<category>\D+)/)(?P<subcategory>\D+)/', views.category, name='subcategory'),
]