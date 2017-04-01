from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from home_page.models import NewLead
from home_page.forms import NewLead,UserForm,UserProfileInfoForm
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
	return render(request,'dashboard/home.html')
@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('home_page:index'))