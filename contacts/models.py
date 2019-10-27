# Imports
from django.db import models

# Contact
class Contact(models.Model):
	listing = models.CharField(max_length=255)
	listing_id = models.IntegerField()
	name = models.CharField(max_length=255)
	name = models.EmailField(max_length=100)
	phone = models.CharField(max_length=100)
	message = models.TextField(max_length=500, blank=True)
	contact_date = models.DateTimeField(auto_now_add=True, blank=True)
	user_id = models.IntegerField(blank=True)

	def __str__(self):
		return self.name
