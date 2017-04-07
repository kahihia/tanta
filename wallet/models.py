from django.db import models

# Create your models here.
class TantaWallet(models.Model):
	usr = models.ForeignKey('auth.User')
	wallet=models.DecimalField(max_digits=5,decimal_places=2)

	def transaction(self):
		self.save()
	def __str__(self):
		return self.title