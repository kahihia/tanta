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
	('GHS','Ghanaian Cedi'),)

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
		elif currency=='GHS':
			sender_start=sender.local
			recipient_start=recipient.local

		return sender_start, recipient_start

	def grab_forex(self,user,currency):
		if currency=='USD':
				user_start=user.dollars
		elif currency=='EUR':
			user_start=user.euros
		elif currency=='GBP':
			user_start=user.pounds
		elif currency=='GHS':
			user_start=user.local
		return user_start

	
	def transaction_send(self,sender_start,amount):
		if sender_start < amount:
			return "Insufficient Funds"
		else:
			sender_final=sender_start - amount
		return sender_final
	
	def transaction_recieve(self,recipient_start,amount):
		recipient_final=recipient_start + amount
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
		elif currency=='GHS':
			sender.local=sender_final
			recipient.local=recipient_final
		self.save()

	def commit_forex(self,user,currency,user_amount):
		if currency=='USD':
			user.dollars=user_amount
		elif currency=='EUR':
			user.euros=user_amount
		elif currency=='GBP':
			user.pounds=user_amount
		elif currency=='GHS':
			user.local=user_amount
		self.save()



	def __str__(self):
		return str(self.user) + str(self.user.id)

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

		

class ForexRates(models.Model):
	date=models.DateTimeField(default=timezone.now)
	dollars=models.DecimalField(default=0,decimal_places=2,max_digits=9)
	euros=models.DecimalField(default=0,decimal_places=2,max_digits=9)
	pounds=models.DecimalField(default=0,decimal_places=2,max_digits=9)
	cedis=models.DecimalField(default=0,decimal_places=2,max_digits=9)
	shillings=models.DecimalField(default=0,decimal_places=2,max_digits=9)
	pesos=models.DecimalField(default=0,decimal_places=2,max_digits=9)
	naira=models.DecimalField(default=0,decimal_places=2,max_digits=9)
	swkrone=models.DecimalField(default=0,decimal_places=2,max_digits=9)
	nwkrone=models.DecimalField(default=0,decimal_places=2,max_digits=9)
	indrp=models.DecimalField(default=0,decimal_places=2,max_digits=9)
	chny=models.DecimalField(default=0,decimal_places=2,max_digits=9)
	ausd=models.DecimalField(default=0,decimal_places=2,max_digits=9)
	saud=models.DecimalField(default=0,decimal_places=2,max_digits=9)
	rurub=models.DecimalField(default=0,decimal_places=2,max_digits=9)

	def grab_exchange_currency(self,currency):
		if currency=='USD':
				curr_return=self.dollars
		elif currency=='EUR':
			curr_return=self.euros
		elif currency=='GBP':
			curr_return=self.pounds
		elif currency=='GHS':
			curr_return=self.cedis
		return curr_return

	def convert_currency_to_dollar(self,currency_have,amount):
		if currency_have=='USD':
				curr_dollar=(1/self.dollars)*amount
		elif currency_have=='EUR':
			curr_dollar=(1/self.euros)*amount
		elif currency_have=='GBP':
			curr_dollar=(1/self.pounds)*amount
		elif currency_have=='GHS':
			curr_dollar=(1/self.cedis)*amount
		return curr_dollar

	def convert_currency_from_dollar(self,currency_want,curr_dollar):
		if currency_want=='USD':
				final_amount=(self.dollars)*curr_dollar
		elif currency_want=='EUR':
			final_amount=(self.euros)*curr_dollar
		elif currency_want=='GBP':
			final_amount=(self.pounds)*curr_dollar
		elif currency_want=='GHS':
			final_amount=(self.cedis)*curr_dollar
		return final_amount


	def __str__(self):
		return str(self.date)