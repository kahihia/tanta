from django.db import models
from django.contrib.auth.models import User

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

	

	#additional

	profile_pic=models.ImageField(upload_to='profile_pic',blank=True)

	def __str__(self):
		return self.user.username
