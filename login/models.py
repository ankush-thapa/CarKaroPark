from __future__ import unicode_literals
import uuid
from django.db import models

# Create your models here.

class Person(models.Model):
	name = models.CharField(max_length = 50)
	email = models.EmailField(max_length = 70)
	passw = models.CharField(max_length = 120)
	car_reg = models.CharField(max_length = 80)
	phone = models.IntegerField(max_length = 10)

class Person_Meta(models.Model):
	customer_id = models.UUIDField(primary_key=True,editable = False)
	staff = models.BooleanField()
