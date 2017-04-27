from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.views.generic import (TemplateView,CreateView,DetailView,ListView,UpdateView,DeleteView)
from wallet.models import Wallet,Transactions,ForexRates,Settings,GroupMember,Group
from wallet.forms import TransferForm,ForexForm,SettingsForm,GroupForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from decimal import *
from django.db.models.signals import post_save
from django.db.models import Q
# Create your views here.
def wallet_summary(request):
	return render(request,'wallet_summary.html',)

def transfer(request, *args, **kwargs):
	user=request.user
	transfer = TransferForm()
	sender=Wallet.objects.get(user=request.user)
	if request.method=='POST':
		transfer =TransferForm(request.POST)
		if transfer.is_valid():
			transferamnt=Decimal(transfer['amount'].value())
			recipient=transfer['user'].value()
			currency=transfer['currency'].value()
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

		return render(request,'thanks.html',{'transfer':transferamnt,'denom':currency,})
	return render(request,'transfer.html',{'form':transfer,})

def info(request):
	return render(request,'info.html')
	
def forex(request):
	user=Wallet.objects.get(user=request.user)
	tanta_fx=Wallet.objects.get(user=9)
	rates=ForexRates.objects.get(date__lte=timezone.now())
	forex=ForexForm()
	if request.method=='POST':
		forex=ForexForm(request.POST)
		if forex.is_valid():
			currency_want=forex['currency_want'].value()
			currency_have=forex['currency_have'].value()
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
	form=SettingsForm()
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

def p2p(request):
	return render(request, 'p2p.html')

def groups(request):
	try:
		user=GroupMember.objects.get(person=request.user)
	except:
		user=GroupMember.objects.create(person=request.user)
	form=GroupForm()
	if request.method=='POST':
		form=GroupForm(request.POST)
		redirect_to=request.POST.get('next','')
		if form.is_valid():
			group=form['group'].value()
			group=Group.objects.get(id=group)
			user.group=group
			user.save()
			return HttpResponseRedirect(redirect_to)

	return render(request, 'groups.html',{'form':form})



