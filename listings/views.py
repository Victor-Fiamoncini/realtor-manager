# Imports
from django.shortcuts import render

# Index
def index(request):
	return render(request, 'listings/listings.html')

# Listing
def listing(request):
	return render(request, 'listings/listing.html')

# Search
def search(request):
	return render(request, 'listings/search.html')

