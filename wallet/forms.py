from django import forms
from django.forms import ModelForm
from wallet.models import Wallet, currencies, Settings, GroupMember, Group



class TransferForm(forms.Form):
	amount=forms.DecimalField(min_value=1,decimal_places=2,label='',
		widget=forms.NumberInput(attrs={'placeholder':'Transfer Amount'}))
	recipient=forms.CharField(label='',
		widget=forms.TextInput(attrs={'placeholder':'Enter name or id'}))
		

class ForexForm(forms.Form):
	amount=forms.DecimalField(min_value=1,decimal_places=2,label='',
		widget=forms.NumberInput(attrs={'placeholder':'Exchange Amount'}))
	currency_want=forms.ChoiceField(currencies,label='')

class SettingsForm(forms.ModelForm):
	class Meta:
		model=Settings
		fields=['borrow_lend']

class JoinGroupForm(forms.ModelForm):
	group=forms.ChoiceField()
	class Meta:
		model=Group
		fields=['name']

class TF(forms.Form):
	def __init__(self, user, *args, **kwargs):
		super(TF,self).__init__(*args,**kwargs)
		self.fields['currency'] = forms.ChoiceField(
			choices=[Wallet.objects.filter(user=user).iterator()])

class ContactForm(forms.Form):
	contact_name=forms.CharField(label='',
		widget=forms.TextInput(attrs={'placeholder':'Enter name or phone #'}))
		