from django.db import models
from django.utils import timezone
from django.core.urlresolver import reverse


# Create your models here.
class Post(models.Models):
	author = models.ForeignKey('auth.User')
	title=models.CharField(max_length=500)
	text=models.TextField()
	create_date=modles.DateTimeField(default=timezone.now())
	published_date=models.DateTimeField(blank=True,null=True)

	def publish(self):
		self.published_date=timezone.now()
		self.save()

	def approve_comments(self):
		return self.comments.filter(approved_comments=true)

	def __str__(self):
		return self.title
class Comment(object):
	post=models.ForeignKey('blog.Post',related_name='coments')
	author=models.CharField(max_length=200)
	text=models.TextField()
	create_date=models.DateTimeField(default=timezone.now())
	approve_comment=models.BooleanField(default=False)