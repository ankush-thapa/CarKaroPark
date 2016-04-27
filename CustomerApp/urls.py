from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
	
	url(r'^login/$', views._login, name='_login'),
	url(r'^regiter/$',views.register),

]
