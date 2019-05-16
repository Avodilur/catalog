from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', name='monitor'),
    url(r'^(?P<elem>[a-z]+)&(?P<elem_id>[0-9]+)/$')
]