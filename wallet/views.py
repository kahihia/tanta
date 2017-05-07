from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import update_session_auth_hash
from django.utils import timezone
from django.views.generic import (TemplateView,CreateView,DetailView,ListView,UpdateView,DeleteView)
from wallet.models import Wallet,Transactions,ForexRates,Settings,GroupMember,Group,Contacts,Social
from wallet.forms import TransferForm,ForexForm,SettingsForm,ContactForm,JoinGroupForm
from home_page.models import UserProfileInfo
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from decimal import *
from django.db.models.signals import post_save
from django.db.models import Q
from datetime import datetime, timedelta
from django.core import serializers
# Create your views here.
def wallet_summary(request):
	return render(request,'wallet_summary.html',)

def transfer(request):
	user=request.user
	sender=Wallet.objects.get(user=request.user)
	transfer = TransferForm()
	if request.method=='POST':
		transfer =TransferForm(request.POST)
		if transfer.is_valid():
			transferamnt=Decimal(transfer['amount'].value())
			recipient=transfer['recipient'].value()
			currency=request.POST['curr']
			try:
				try:
					contact_user=User.objects.get(username=recipient)
					recipient_id=contact_user.id
					recipient=Wallet.objects.get(user=recipient_id)
				except:
					return render(request,'partials/_invalid_user.html')
			except:
				try:
					recipient=Wallet.objects.get(user=recipient)
				except:
					return render(request,'partials/_invalid_user.html')
		try:
			send_start,recieve_start = sender.grab_values(sender,recipient,currency)
		except:
			return render(request, 'partials/_self_send_error.html')

		if sender.transaction_send(send_start,transferamnt) == "Insufficient Funds":
			return render(request,'partials/_insufficient.html')
		else:
			send_final=sender.transaction_send(send_start,transferamnt)
		recip_final=recipient.transaction_recieve(recieve_start,transferamnt)
		sender.commit_transaction(sender,recipient,currency,send_final,recip_final)
		
		recipient.commit_transaction(sender,recipient,currency,send_final,recip_final)
		Transactions.objects.save_record(sender,recipient,transferamnt,currency)

		return render(request,'thanks.html',{'transfer':transferamnt,'denom':currency})
	return render(request,'transfer.html',{'form':transfer,})

def info(request):
	return render(request,'info.html')

def passreset(request):
	form=PasswordChangeForm(user=request.user)
	if request.method =='POST':
		form=PasswordChangeForm(user=request.user,data=request.POST)
		redirect_to = request.POST.get('next')
		if form.is_valid():
			form.save()
			update_session_auth_hash(request,form.user)
			return HttpResponseRedirect(redirect_to)
	return render(request,'pword.html',{'form':form})
	
def forex(request):
	user=Wallet.objects.get(user=request.user)
	tanta_fx=Wallet.objects.get(user=9)
	rates=ForexRates.objects.get(date__lte=timezone.now())
	time_range=datetime.now() - timedelta(days=1)
	results=Transactions.objects.filter(fx=request.user).filter(transfer_date__gt=time_range)
	if results.count() >= 3:
		return render(request,'partials/_toomanyfx.html')
	else:
		forex=ForexForm()
		if request.method=='POST':
			forex=ForexForm(request.POST)
			if forex.is_valid():
				currency_want=forex['currency_want'].value()
				currency_have=request.POST['curr']
				amount=Decimal(forex['amount'].value())
				if currency_want == currency_have:
					return render(request, 'partials/_currency_error.html')
	# GRAB THE CURRENCY THAT THE USER HAS USING WALLET MODEL
				user_start_have=user.grab_forex(user,currency_have)
				forex_start_have=tanta_fx.grab_forex(tanta_fx,currency_have)
				user_start_want=user.grab_forex(user,currency_want)
				forex_start_want=tanta_fx.grab_forex(tanta_fx,currency_want)

	# SUBTRACT THE AMOUNT THAT THE USER WANTS TO EXCHANGE FROM THEIR WALLET 
	#AND INTO FOREX WALLET USING WALLET MODEL
				if user.transaction_send(user_start_have,amount)=='Insufficient Funds':
					return render(request,'partials/_insufficient.html')
				else:
					user_get=user.transaction_send(user_start_have,amount)
					forex_get=tanta_fx.transaction_recieve(forex_start_have,amount)
					user.commit_forex(user,currency_have,user_get)
					tanta_fx.commit_forex(tanta_fx,currency_have,forex_get)
			# CONVERT TRANSFER CURRENCY INTO DOLLARS 
				curr_dollar=rates.convert_currency_to_dollar(currency_have,amount)
			#AND THEN INTO WANTED CURRENCY
				final_currency=round(rates.convert_currency_from_dollar(currency_want,curr_dollar),2)
			# ADD TRANSFERED FUNDS FROM FOREX WALLET INTO USER WALLET
				forex_final=tanta_fx.transaction_send(forex_start_want,final_currency)
				user_final=user.transaction_recieve(user_start_want,final_currency)
				user.commit_forex(user,currency_want,user_final)
				tanta_fx.commit_forex(tanta_fx,currency_want,forex_final)

				Transactions.objects.save_forex(user,amount,currency_have,final_currency,currency_want)
				
				return render(request, 'forex_thanks.html',{'amount':amount, 'ch':currency_have, 'fc':final_currency, 'cw':currency_want})

				
		return render(request,'forex.html',{'form2':forex})

def settings(request):
	try:
		user=Settings.objects.get(user=request.user)
	except:
		user=Settings.objects.create(user=request.user)
	form=SettingsForm(initial={'borrow_lend':user.borrow_lend})
	if request.method=='POST':
		form=SettingsForm(request.POST)
		redirect_to = request.POST.get('next','')
		if form.is_valid():
			borrow_lend=form['borrow_lend'].value()
			user.borrow_lend=borrow_lend
			user.save()
		return HttpResponseRedirect(redirect_to)

	return render(request,'settings.html',{'form':form})

def contacts(request):
	return render(request,'contacts.html')

def add_contacts(request):
	form=ContactForm()
	if request.method=='POST':
		form=ContactForm(request.POST)
		redirect_to = request.POST.get('next','')
		if form.is_valid():
			contact_name=form['contact_name'].value()
			### GRAB THE VALUE FROM EITHER PHONE OR USERNAME
			try:
				try:
					contact_user=User.objects.get(username=contact_name)
				except:
					return render(request,'partials/_invalid_user.html')
			except:
				try:
					contact=UserProfileInfo.objects.get(phone_number=contact_name)
				except:
					return render(request,'partials/_invalid_user.html')
			
			# IF THE A USERNAME IS ENTERED:
			try:
				contact_id=contact_user.id
				contact_user=contact_user.username
				contact_phone=UserProfileInfo.objects.get(user=contact_id)
				if Contacts.objects.filter(user=request.user,name=contact_user).exists():
					return HttpResponseRedirect(redirect_to)
				else:
					Contacts.objects.save_contact(request.user,contact_user,contact_phone)
					return HttpResponseRedirect(redirect_to)
			# IF A PHONE NUMBER IS ENTERED:

			except NameError:
				contact_phone=form['contact_name'].value()
				contact=User.objects.get(username=contact.user)
				contact_name=contact.username
			if Contacts.objects.filter(user=request.user,name=contact_name).exists():
				return HttpResponseRedirect(redirect_to)
			else:
				Contacts.objects.save_contact(request.user,contact_name,contact_phone)
				return HttpResponseRedirect(redirect_to)
	
	return render(request, 'add_contact.html', {'form':form})

def p2p(request):
	return render(request, 'p2p.html')

def groups(request):
	form=JoinGroupForm()
	if request.method=='POST':
		redirect_to=request.POST.get('next','')
		groups=request.POST.getlist('group')
		user=GroupMember.objects.create(person=request.user)
		for item in groups:
			group=Group.objects.get(name=item)
			user.group=group
			user.person=request.user
			user.save()
		return HttpResponseRedirect(redirect_to)

	return render(request, 'groups.html',)

def display_groups(request):
	group_type=request.GET.get('type',None)
	group_type=group_type.lower()
	type_query=Group.objects.filter(group_type=group_type)
	data=serializers.serialize('json',type_query)
	return HttpResponse(data,'json')



