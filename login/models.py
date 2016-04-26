from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import user

from uuid import UUID
# Create your models here.

class Customer(models.User):
	username = models.CharField(max_length=30)
	email = models.EmailField(max_length=40)
	password = models.CharField(max_length=20)
	is_staff = models.BooleanField()
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	
	mobile = CharField(max_length=10)
	guest_user = models.BooleanField()
	car_reg_no = CharField(max_length=10)