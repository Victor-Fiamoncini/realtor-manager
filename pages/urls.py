# Imports
from django.urls import path
from . import views

# Pages urls
urlpatterns = [
	path('', views.index, name='index'),
	path('about', views.about, name='about'),
]
