from django.shortcuts import render
from django.http import HttpResponse

from .forms import loginForm
# Create your views here.

def get_name(request):
	if request.method == 'POST':
		form=loginForm(request.POST)
		if form.is_valid():
			return HttpResponse('Login uNSuccessful')
	else:
		form = loginForm()
		return HttpResponse('Login Successful')