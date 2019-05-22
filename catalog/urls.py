from django.conf.urls import url
from . import views


urlpatterns = [
    # url(r'^$', views.category, name='catalog'),
    url(r'^(\w+)*[/]?[(d+)]*', views.category, name='category'),
]