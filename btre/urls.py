# Imports
from django.contrib import admin
from django.urls import path, include

# Urls
urlpatterns = [
  path('admin/', admin.site.urls),
	path('', include('pages.urls')),
]
