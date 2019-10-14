# Imports
from django.contrib import admin
from .models import Realtor

# RealtorAdmin
class RealtorAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'email', 'hire_date')
	list_display_links = ('id', 'name')
	search_fields = ('name', 'email')
	list_per_page = 25

# Add realtors to dashboard
admin.site.register(Realtor, RealtorAdmin)
