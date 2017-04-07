from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.views.generic import (TemplateView,CreateView,DetailView,ListView,UpdateView,DeleteView)
from wallet.models import Wallet
from wallet.forms import TransferForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q,F

# Create your views here.
def wallet_summary(request):
	return render(request,'wallet_summary.html')
def transfer(request):
	form = TransferForm()
	balance=Wallet.objects.get(user=request.user)
	if request.method=='POST':
		form =TransferForm(request.POST)
		if form.is_valid():
			transferamnt=form['amount'].value()
			balance.balance=float(balance.balance) - float(transferamnt)
			balance.save()
			return render(request,'thanks.html',{'transfer':transferamnt})
	return render(request,'transfer.html',{'form':form})