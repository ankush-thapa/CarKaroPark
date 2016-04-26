from django import forms

class loginForm(forms.Form):
	email=forms.CharField(label='Email', max_length=100)
	