from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

# Create your models here.
currencies=(
	('USD','United States Dollar'),
	('GBP','British Pound'),
	('EUR','Euro'),
	('GHC','Ghanaian Cedi'),)

class Wallet(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	dollars=models.DecimalField(max_digits=7,decimal_places=2,default=0)
	euros=models.DecimalField(max_digits=7,decimal_places=2,default=0)
	pounds=models.DecimalField(max_digits=7,decimal_places=2,default=0)
	local=models.DecimalField(max_digits=7,decimal_places=2,default=0)

	
###### WRITE METHODS FOR TRANSACTIONS: EG VERIFY USER, CHECK AMOUNT, ETC. #####
	def transaction(self,sender,recipient,amount,currency):

		if currency=='USD':
				sender_balance=sender.dollars
				recipient_balance=recipient.dollars
		elif currency=='EUR':
			sender_balance=sender.euros
			recipient_balance=recipient.euros
		elif currency=='GBP':
			sender_balance=sender.pounds
			recipient_balance=recipient.pounds
		elif currency=='GHC':
			sender_balance=sender.local
			recipient_balance=recipient.local
		if float(sender_balance) < float(amount):
			return "Insufficient Funds"
		else:
			recipient_balance=float(recipient_balance) + float(amount)
			sender_balance=float(sender_balance) - float(amount)
		
		self.save()



	def __str__(self):
		return str(self.dollars)