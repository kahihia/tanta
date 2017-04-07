from django.shortcuts import render
from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.views.generic import (TemplateView,CreateView,DetailView,ListView,UpdateView,DeleteView)
from wallet.models import Wallet
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.
# class WalletSummary(ListView):
# 	model=TantaWallet
		
class WalletUpdate(UpdateView):
	model=Wallet
	fields=['balance']
		
def wallet_summary(request):
	#summ=TantaWallet.objects.get()
	# context_dict={'summary':summ}
	return render(request,'wallet_summary.html')