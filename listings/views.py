# Imports
from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing

# Index
def index(request):
	listings = Listing.objects.all()

	paginator = Paginator(listings, 3)
	page = request.GET.get('page')
	paged_listings = paginator.get_page(page)

	context = {
		'listings': paged_listings
	}
	return render(request, 'listings/listings.html', context)

# Listing
def listing(request, listing_id):
	return render(request, 'listings/listing.html')

# Search
def search(request):
	return render(request, 'listings/search.html')
