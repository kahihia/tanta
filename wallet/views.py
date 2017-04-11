from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.views.generic import (TemplateView,CreateView,DetailView,ListView,UpdateView,DeleteView)
from wallet.models import Wallet
from wallet.forms import TransferForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django import forms
from decimal import *
from django.db.models.signals import post_save
from actstream import action
from actstream.models import user_stream

# Create your views here.
def wallet_summary(request):
	# user_stream(request.user, with_user_activty=True)

	return render(request,'wallet_summary.html')
def transfer(request):
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
				return render(request,'invalid_user.html')
	
		send_start,recieve_start = sender.grab_values(sender,recipient,currency)
		if sender.transaction_send(send_start,transferamnt) == "Insufficient Funds":
			return render(request,'insufficient.html')
		else:
			send_final=sender.transaction_send(send_start,transferamnt)
		recip_final=recipient.transaction_recieve(recieve_start,transferamnt)
		sender.commit_transaction(sender,recipient,currency,send_final,recip_final)
		recipient.commit_transaction(sender,recipient,currency,send_final,recip_final)
		# action.send(request.user,verb='transfered', action_object=transferamnt+currency, target=recipient)

		return render(request,'thanks.html',{'transfer':transferamnt,'denom':currency,})
	return render(request,'transfer.html',{'form':transfer,})
def info(request):
	return render(request,'info.html')




