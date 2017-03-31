from django.shortcuts import render
from home_page.models import NewLead
from home_page.contact_form import NewLead

# Create your views here.
def index(request):
	return render(request,'home_page/home.html')
def contact(request):
	form=NewLead(auto_id=False)
	if request.method=='POST':
		form=NewLead(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return thanks(request)



	return render(request,'home_page/contact.html',{'form':form})
def about(request):
	return render(request,'home_page/about.html')
def thanks(request):
	return render(request,'home_page/thank_you.html')
def onyx(request):
	return render(request,'home_page/onyx.html')