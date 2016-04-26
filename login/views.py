from django.shortcuts import render, HttpResponse
from .models import *
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
	return HttpResponse("YYAYAYAYAYAYAY")

def login(request, mail , passw):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username = Person.object.get(mail), password = Person.object.get(passw))
	if user is not None:
		if user.is_active:
			login(request, user)
		else :
			return HttpResponse("Invalid username or password")

		return HttpResponse("Logged in as user this")
	 
def logout(request):
	logout(request)
	return HttpResponse ("Logged out!")

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponse("Successfully created user")
		else:
			form = UserCreationForm()
		# render the same form again named registration.html in registartion app	
		return render(request, "register/registration.html",{ 
			'form' : form,
		})