from django import forms
from django.forms import ModelForm
from wallet.models import Wallet, currencies, Settings, GroupMember, Group
from django.db.models import Q



class TransferForm(forms.Form):
	amount=forms.DecimalField(min_value=1,decimal_places=2,label='',
		widget=forms.NumberInput(attrs={'placeholder':'Transfer Amount'}))
	user=forms.IntegerField(label='',
		widget=forms.NumberInput(attrs={'placeholder':"Enter recipient's id"}))

class TForm(forms.ModelForm):
	currency = forms.ModelChoiceField(queryset=Wallet.objects.filter(user=7,euros__gt=0))
	class Meta:
		model=Wallet
		fields=['dollars','euros']
		

class ForexForm(forms.Form):
	amount=forms.DecimalField(min_value=1,decimal_places=2,label='',
		widget=forms.NumberInput(attrs={'placeholder':'Exchange Amount'}))
	currency_want=forms.ChoiceField(currencies,label='')

class SettingsForm(forms.ModelForm):
	class Meta:
		model=Settings
		fields=['borrow_lend']

class JoinGroupForm(forms.ModelForm):
	group=forms.ModelChoiceField(queryset=Group.objects.all())
	class Meta:
		model=Group
		fields=['name']


class GroupForm(forms.Form):
	def __init__(self,*args,**kwargs):
		super(GroupForm,self).__init__(*args,**kwargs)
		self.fields['group'] = forms.ChoiceField(
			choices=[(o.id,str(o)) for o in Group.objects.all()])

class TF(forms.Form):
	def __init__(self, user, *args, **kwargs):
		super(TF,self).__init__(*args,**kwargs)
		self.fields['currency'] = forms.ChoiceField(
			choices=[Wallet.objects.filter(user=user).iterator()])

class ContactForm(forms.Form):
	contact_name=forms.CharField(label='',)
		