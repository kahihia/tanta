from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request,'home_page/home.html')
def contact(request):
	return render(request,'home_page/contact.html')
def about(request):
	return render(request,'home_page/about.html')