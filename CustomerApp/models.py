from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

from uuid import UUID
# Create your models here.

class Customer(User):
	#usrname = models.CharField(max_length=30)
	#mail = models.EmailField(max_length=40)
	#passw = models.CharField(max_length=20)
	#staff = models.BooleanField(default=False)
#	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	mobile = models.CharField(max_length=10)
	guest_user = models.BooleanField()
	car_reg_no = models.CharField(max_length=10)
