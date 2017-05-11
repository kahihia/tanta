from django import forms
from django.forms import ModelForm
from wallet.models import Wallet, currencies, Settings, GroupMember, Group



class TransferForm(forms.Form):
	amount=forms.DecimalField(min_value=1,decimal_places=2,label='',
		widget=forms.NumberInput(attrs={'placeholder':'Transfer Amount'}))
	recipient=forms.CharField(label='',required=False,
		widget=forms.TextInput(attrs={'placeholder':'Enter name or id'}))
		

class ForexForm(forms.Form):
	amount=forms.DecimalField(min_value=1,decimal_places=2,label='',
		widget=forms.NumberInput(attrs={'placeholder':'Exchange Amount'}))
	currency_want=forms.ChoiceField(currencies,label='')

class SettingsForm(forms.ModelForm):
	class Meta:
		model=Settings
		fields=['borrow_lend']

class ContactForm(forms.Form):
	contact_name=forms.CharField(label='',
		widget=forms.TextInput(attrs={'placeholder':'Enter name or phone #'}))
class GroupForm(forms.ModelForm):
	class Meta:
		model=Group
		fields=['name','group_type']
	def clean(self):
		cleaned_data=super().clean()
		name=self.cleaned_data['name']
		try:
			Group.objects.get(name=name)
			raise forms.ValidationError('Group already exists')
		except:
			pass