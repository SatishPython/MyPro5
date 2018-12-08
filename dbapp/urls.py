from django.conf.urls import url
from . import views
app_name="dbapp"
urlpatterns=[
    url(r'^$',views.Input,name='input'),
    url(r'^insert$',views.Insert,name='insert'),
    url(r'^display$',views.Display,name='display'),
]