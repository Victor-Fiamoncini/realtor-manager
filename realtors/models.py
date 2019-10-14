# Imports
from django.db import models
from datetime import datetime

# Realtor
class Realtor(models.Model):
	name = models.CharField(max_length=255)
	photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
	description = models.TextField(blank=True)
	phone = models.CharField(max_length=20)
	email = models.EmailField(max_length=255)
	is_mvp = models.BooleanField(default=False)
	hire_date = models.DateTimeField(default=datetime.now, blank=True)

	# To string
	def __str__(self):
		return self.name
