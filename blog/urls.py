from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.test,name="test"),
    url(r'^all_post/$', views.all_post, name="all_post"),
    url(r'^insert_post/$', views.insert_post, name="insert_post")
]