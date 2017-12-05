from django.conf.urls import url, include
from . import views

app_name = 'shorty'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/', views.create, name='create'),
    url(r'^(?P<code>\w+)$', views.redirect, name='redirect'),
]
