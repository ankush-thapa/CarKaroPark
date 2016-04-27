from django.shortcuts import render, HttpResponse
from .models import *
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

from CustomerApp import models



def index(request):
	return HttpResponse("YYAYAYAYAYAYAY")

def register(request):
	name = request.POST["name"]
	username = request.POST["username"]
	password = request.POST["password"]
	conf_passw = request.POST["confirm_password"]
	email = request.POST["email"]
	if request.method == 'POST':
		if password != confirm_password:
			return HttpResponse("Passwords do not match")
		#email validation code as per queryset in django
		#.......
		#.......

		try:
			customer = Customer()
			customer.username = username
			customer.firt_name = name
			customer.email = email
			customer.save()
		except:
			return HttpResponse("This email id is already registered")
		customer.set_password(password)
		customer.save()
		return HttpResponse("Customer registered successfully.")

def _login(request):

	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username = Person.object.get(email), password = Person.object.get(password))
	if user is not None:
		if user.is_active:
			login(request, user)
		else :
			return HttpResponse("Invalid username or password")

		return HttpResponse("Logged in as user this")
	 
