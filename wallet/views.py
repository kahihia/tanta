from django.shortcuts import render
from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.views.generic import (TemplateView,CreateView,DetailView,ListView,UpdateView,DeleteView)
from wallet.models import Wallet
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.
def wallet_summary(request):
	return render(request,'wallet_summary.html')
def transfer(request):
	users=Wallet.objects.all()
	context_dict={'users':users}
	return render(request,'transfer.html',context=context_dict)