from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.db.models import F
# Create your models here.
currencies=(
	('USD','United States Dollar'),
	('GBP','British Pound'),
	('EUR','Euro'),
	('GHC','Ghanaian Cedi'),)

class Wallet(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	dollars=models.FloatField(default=0)
	euros=models.FloatField(default=0)
	pounds=models.FloatField(default=0)
	local=models.FloatField(default=0)

	
###### WRITE METHODS FOR TRANSACTIONS: EG VERIFY USER, CHECK AMOUNT, ETC. #####
	def grab_values(self,sender,recipient,currency):
		if currency=='USD':
				sender_start=sender.dollars
				recipient_start=recipient.dollars
		elif currency=='EUR':
			sender_start=sender.euros
			recipient_start=recipient.euros
		elif currency=='GBP':
			sender_start=sender.pounds
			recipient_start=recipient.pounds
		elif currency=='GHC':
			sender_start=sender.local
			recipient_start=recipient.local
		return sender_start, recipient_start
	
	def transaction_send(self,sender_start,amount):
		if sender_start < amount:
			return "Insufficient Funds"
		else:
			sender_final=sender_start - amount
		return sender_final
	def transaction_recieve(self,recipient_start,amount):
		recipient_final=recipient_start+amount
		return recipient_final
	def commit_transaction(self,sender,recipient,currency,sender_final,recipient_final):
		if currency=='USD':
			sender.dollars=sender_final
			recipient.dollars=recipient_final
		elif currency=='EUR':
			sender.euros=sender_final
			recipient.euros=recipient_final
		elif currency=='GBP':
			sender.pounds=sender_final
			recipient.pounds=recipient_final
		elif currency=='GHC':
			sender.local=sender_final
			recipient.local=recipient_final
		self.save()



	def __str__(self):
		return str(self.user)