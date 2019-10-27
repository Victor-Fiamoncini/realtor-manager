# Imports
from django.shortcuts import render, redirect

# Login
def login(request):
	return render(request, 'accounts/login.html')

# Register
def register(request):
	return render(request, 'accounts/register.html')

# Logout
def logout(request):
	return redirect('index')

# Dashboard
def dashboard(request):
	return render(request, 'accounts/dashboard.html')
