from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from home_page.models import NewLead
from home_page.forms import NewLead,UserForm,UserProfileInfoForm
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
	return render(request,'home_page/home.html')

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('home_page:index'))

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
def getstarted(request):
	registered=False

	if request.method =='POST':
		user_form =UserForm(data=request.POST)
		profile_form=UserProfileInfoForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user=user_form.save()
			user.set_password(user.password)
			user.save()

			profile=profile_form.save(commit=False)
			profile.user=user

			if 'profile_pic' in request.FILES:
				profile.profile_pic=request.FILES['profile_pic']
				profile.save()

			registered=True
		else:
			print(user_form.errors,profile_form.errors)
	else:
		user_form=UserForm()
		profile_form=UserProfileInfoForm()
		
	return render(request,'home_page/getstart.html',
		{'user_form':user_form,'profile_form':profile_form,
		'registered':registered})
def signin(request):
	if request.method == 'POST':
		username=request.POST.get('username','')
		password=request.POST.get('password','')
		user=authenticate(username=username,password=password)

		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect(reverse('home_page:index'))
			else:
				return HttpResponse('Account not active')
		else:
			return HttpResponse('User does not exist')
	else:
		return render(request,'home_page/sign_in.html')