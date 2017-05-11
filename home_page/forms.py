from django import forms
from django.core import validators
from home_page.models import NewLead
from django.contrib.auth.models import User
from home_page.models import UserProfileInfo


class NewLead(forms.ModelForm):
	class Meta:
		model=NewLead
		fields='__all__'
		labels={
		''
		}
		widgets={
		'name' : forms.TextInput(attrs={'placeholder':'Name'}),
		'email': forms.TextInput(attrs={'placeholder':'Email'}),
		'verify_email':forms.TextInput(attrs={'placeholder':'Verify Email'}),
		'business':forms.TextInput(attrs={'placeholder':'Business Name'}),
		'text':forms.Textarea(attrs={'cols':100,'rows':10,'placeholder':'Describe your project. What problems are you facing? What ideas do you have?'})
		}
		
	def clean(self):
		all_clean_data=super().clean()
		email=all_clean_data['email']
		vmail=all_clean_data['verify_email']
		if email != vmail:
			raise forms.ValidationError("Make sure emails match")


class UserForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput())

	class Meta():
		model=User
		fields=('username','password')
	def clean_username(self):
		username=self.cleaned_data['username']
		username.lower()
		try:
		 	User.objects.get(username=username)
		 	raise forms.ValidationError('Username taken')
		except:
			pass
		return username

class UserProfileInfoForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(UserProfileInfoForm, self).__init__(*args, **kwargs)
		self.fields['phone_number'].required = True
	class Meta():
		model=UserProfileInfo
		fields=['phone_number']