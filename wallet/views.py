from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.views.generic import (TemplateView,CreateView,DetailView,ListView,UpdateView,DeleteView)
from wallet.models import Wallet,Transactions,ForexRates
from wallet.forms import TransferForm,ForexForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from decimal import *
from django.db.models.signals import post_save
from actstream import action
from actstream.models import user_stream
from django.db.models import Q
# Create your views here.
def wallet_summary(request):
	return render(request,'wallet_summary.html',)
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
		try:
			send_start,recieve_start = sender.grab_values(sender,recipient,currency)
		except:
			return render(request, 'self_send_error.html')

		if sender.transaction_send(send_start,transferamnt) == "Insufficient Funds":
			return render(request,'insufficient.html')
		else:
			send_final=sender.transaction_send(send_start,transferamnt)
		recip_final=recipient.transaction_recieve(recieve_start,transferamnt)
		sender.commit_transaction(sender,recipient,currency,send_final,recip_final)
		
		recipient.commit_transaction(sender,recipient,currency,send_final,recip_final)
		# activity=action.send(request.user,verb='transfered', action_object=Wallet, target=recipient)
		Transactions.objects.save_record(sender,recipient,transferamnt,currency)

		return render(request,'thanks.html',{'transfer':transferamnt,'denom':currency,})
	return render(request,'transfer.html',{'form':transfer,})
def info(request):
	return render(request,'info.html')
class RecentActivityView(ListView):
	model = Transactions

	def get_queryset(self):
		# user=request.user
		return Transactions.objects.filter(Q(sender=self.request.user,transfer_date__lte=timezone.now()) | Q(reciever=self.request.user,transfer_date__lte=timezone.now())).order_by('transfer_date')


def forex(request):
	user=Wallet.objects.get(user=request.user)
	tanta_fx=Wallet.objects.get(user=9)
	forex=ForexForm()
	if request.method=='POST':
		forex=ForexForm(request.POST)
		if forex.is_valid():
			  pass
			
	return render(request,'forex.html',{'form2':forex})

class ForexRatesView(ListView):
	model = ForexRates

	def get_queryset(self):
		return ForexRates.objects.filter(date__lte=timezone.now()).order_by('date')


