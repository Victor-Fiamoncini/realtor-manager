# Imports
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

# Urls
urlpatterns = [
  # Admin
	path('admin/', admin.site.urls),
	# '/'
	path('', include('pages.urls')),
	# '/accounts/'
	path('accounts/', include('accounts.urls')),
	# /listings/
	path('listings/', include('listings.urls')),
	# '/contacts/'
	path('contacts/', include('contacts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
