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

# Create your views here.
def wallet_summary(request):
	return render(request,'wallet_summary.html')
def transfer(request):
	form = TransferForm()
	sender=Wallet.objects.get(user=request.user)
	if request.method=='POST':
		form =TransferForm(request.POST)
		if form.is_valid():
			transferamnt=form['amount'].value()
			recipient=form['user'].value()
			try:
				recipient=Wallet.objects.get(user=recipient)
			except:
				HttpResponse("User doesn't exist")

			recipient.balance=float(recipient.balance) + float(transferamnt)
			sender.balance=float(sender.balance) - float(transferamnt)
			sender.save()
			recipient.save()
			return render(request,'thanks.html',{'transfer':transferamnt})
	return render(request,'transfer.html',{'form':form})
def info(request):
	return render(request,'info.html')