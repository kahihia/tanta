from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Wallet(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	balance=models.DecimalField(max_digits=5,decimal_places=2)

	def transaction(self):
		self.save()
	
	def __str__(self):
		return str(self.balance)