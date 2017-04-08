from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Wallet(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	dollars=models.DecimalField(max_digits=7,decimal_places=2,default=0)
	euros=models.DecimalField(max_digits=7,decimal_places=2,default=0)
	pounds=models.DecimalField(max_digits=7,decimal_places=2,default=0)
	local=models.DecimalField(max_digits=7,decimal_places=2,default=0)

	def transaction(self):
		self.save()
	
	def __str__(self):
		return str(self.dollars)