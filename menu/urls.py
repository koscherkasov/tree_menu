from django.conf.urls import url
from .import views

app_name = 'menu'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<selected_item_id>[0-9]+)/$', views.item, name='item')
]