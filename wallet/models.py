from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
# Create your models here.
currencies=(
	('USD','United States Dollar'),
	('GBP','British Pound'),
	('EUR','Euro'),
	('GHC','Ghanaian Cedi'),)

class Wallet(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	dollars=models.DecimalField(default=0,decimal_places=2,max_digits=9)
	euros=models.DecimalField(default=0,decimal_places=2,max_digits=9)
	pounds=models.DecimalField(default=0,decimal_places=2,max_digits=9)
	local=models.DecimalField(default=0,decimal_places=2,max_digits=9)

	
###### WRITE METHODS FOR TRANSACTIONS: EG VERIFY USER, CHECK AMOUNT, ETC. #####
	def grab_values(self,sender,recipient,currency):
		if sender == recipient:
			return "Can't Send Money to yourself!"
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

class TransactionsManager(models.Manager):
	def save_record(self,sender,reciever,amount, currency):
		self.create(sender=sender,reciever=reciever,amount=amount,currency=currency,transfer_date=timezone.now())

class Transactions(models.Model):
	sender=models.CharField(max_length=13)
	reciever=models.CharField(max_length=13)
	amount=models.DecimalField(default=0,decimal_places=2,max_digits=9)
	currency=models.CharField(max_length=5,null=True)
	transfer_date=models.DateTimeField(default=timezone.now)
	objects=TransactionsManager()

	def __str__(self):
		return str(self.sender) + " " +str(self.amount) +str(self.currency) + " " +str(self.reciever)

	
