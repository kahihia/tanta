from django import forms
from django.core import validators
from home_page.models import NewLead


class NewLead(forms.ModelForm):
	class Meta:
		model=NewLead
		fields='__all__'
		widgets={
		'name' : forms.TextInput(attrs={'placeholder':'Name'}),
		'email': forms.TextInput(attrs={'placeholder':'Email'}),
		'verify_email':forms.TextInput(attrs={'placeholder':'Verify Email'}),
		'business':forms.TextInput(attrs={'placeholder':'Business Name'}),
		'text':forms.Textarea(attrs={'placeholder':'Describe your project. What problems are you facing? What ideas do you have?'})
		}
		
	def clean(self):
		all_clean_data=super().clean()
		email=all_clean_data['email']
		vmail=all_clean_data['verify_email']
		if email != vmail:
			raise forms.ValidationError("Make sure emails match")
