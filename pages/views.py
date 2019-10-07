# Imports
from django.shortcuts import render

# Index
def index(request):
	return render(request, 'pages/index.html')

# About
def about(request):
	return render(request, 'pages/about.html')
