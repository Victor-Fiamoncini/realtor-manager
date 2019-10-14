# Imports
from django.shortcuts import render
from .models import Listing

# Index
def index(request):
	listings = Listing.objects.all()
	context = {
		'listings': listings
	}
	return render(request, 'listings/listings.html', context)

# Listing
def listing(request, listing_id):
	return render(request, 'listings/listing.html')

# Search
def search(request):
	return render(request, 'listings/search.html')

