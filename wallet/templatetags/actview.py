from django import template
from wallet.models import Transactions, ForexRates
from django.db.models import Q
from django.utils import timezone

register=template.Library()

@register.inclusion_tag('transactions_list.html', takes_context=True)
def show_activity(context):
	user=context['request'].user
	sent_list=Transactions.objects.filter(sender=user,transfer_date__lte=timezone.now()).order_by('-transfer_date')
	recieved_list=Transactions.objects.filter(reciever=user,transfer_date__lte=timezone.now()).order_by('-transfer_date')
	exchanged_list=Transactions.objects.filter(fx=user,transfer_date__lte=timezone.now()).order_by('-transfer_date')
	rates=ForexRates.objects.filter(date__lte=timezone.now()).order_by('date')



	return {'sent':sent_list,'received':recieved_list,'changed':exchanged_list,'rates':rates}
