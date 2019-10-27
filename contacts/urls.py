# Imports
from django.urls import path
from . import views

# Urls
urlpatterns = [
	path('contact', views.contact, name='contact')
]
