# Imports
from django.contrib import admin
from .models import Listing

# Add listings to dashboard
admin.site.register(Listing)
