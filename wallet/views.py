from django.shortcuts import render
from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.views.generic import (TemplateView,CreateView,DetailView,ListView,UpdateView,DeleteView)
from wallet.models import TantaWallet
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.
def wallet_home(request):
	return render(request,'wallet/wallet_summary.html')
class WalletUpdate(object):
	model=TantaWallet
	fields=['balance']
		
def wallet_summary(request,pk):
	summ=get_object_or_404(TantaWallet,pk=pk)
	return redirect('wallet_home',{'summary':summ})