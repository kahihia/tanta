from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.views.generic import (TemplateView,CreateView,DetailView,ListView,UpdateView,DeleteView)
from wallet.models import Wallet
from wallet.forms import TransferForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q,F
from django.http import HttpResponse
from django import forms

# Create your views here.
def wallet_summary(request):
	return render(request,'wallet_summary.html')
def transfer(request):
	transfer = TransferForm()
	sender=Wallet.objects.get(user=request.user)
	if request.method=='POST':
		transfer =TransferForm(request.POST)
		if transfer.is_valid():
			transferamnt=transfer['amount'].value()
			recipient=transfer['user'].value()
			try:
				recipient=Wallet.objects.get(user=recipient)
			except:
				return render(request,'invalid_user.html')
			if float(sender.balance) < float(transferamnt):
				return render(request,'insufficient.html')
			else:
				recipient.balance=float(recipient.balance) + float(transferamnt)
				sender.balance=float(sender.balance) - float(transferamnt)
				sender.save()
				recipient.save()
			return render(request,'thanks.html',{'transfer':transferamnt})
	return render(request,'transfer.html',{'form':transfer,})
def info(request):
	return render(request,'info.html')