from django.conf.urls import url
from . import views

app_name = 'libcard'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create_lib_entry$', views.create_lib_entry, name='create_lib_entry'),

]