from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.
class NewLead(models.Model):
	name=models.CharField(max_length=40)
	email=models.EmailField(max_length=40)
	verify_email=models.EmailField(max_length=40)
	business=models.CharField(max_length=40)
	text=models.CharField(max_length=400)
	def __str__(self):
		return self.name

class UserProfileInfo(models.Model):
	user=models.OneToOneField(User)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_number = models.CharField(max_length=15,validators=[phone_regex], blank=True)

	def __str__(self):
		return self.user.username
