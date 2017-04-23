from django import template
from wallet.models import Transactions,ForexRates,Wallet,Contacts
from django.db.models import Q
from django.utils import timezone

register=template.Library()

@register.inclusion_tag('partials/_transactions_list.html', takes_context=True)
def show_activity(context):
	user=context['request'].user
	sent_list=Transactions.objects.filter(sender=user,transfer_date__lte=timezone.now()).order_by('-transfer_date')
	recieved_list=Transactions.objects.filter(reciever=user,transfer_date__lte=timezone.now()).order_by('-transfer_date')[:5]
	exchanged_list=Transactions.objects.filter(fx=user,transfer_date__lte=timezone.now()).order_by('-transfer_date')[:5]

	return {'sent':sent_list,'received':recieved_list,'changed':exchanged_list}


@register.inclusion_tag('partials/_rate_list.html')
def show_rates():
	rates=ForexRates.objects.filter(date__lte=timezone.now()).order_by('date')
	
	return{'rates':rates,}

@register.inclusion_tag('partials/_wallet.html', takes_context=True)
def show_wallet(context):
	user=context['request'].user
	wallet_list=Wallet.objects.filter(user=user)
	
	return{'wallet':wallet_list}

@register.inclusion_tag('partials/_quick_balance.html', takes_context=True)
def quick_balance(context):
	user=context['request'].user
	wallet_list=Wallet.objects.filter(user=user)
	
	return{'wallet':wallet_list}

@register.inclusion_tag('partials/_contacts.html', takes_context=True)
def display_contacts(context):
	user=context['request'].user
	contact_list=Contacts.objects.filter(user=user)
	return{'contact_list':contact_list}