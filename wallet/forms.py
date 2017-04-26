from django import forms
from django.forms import ModelForm
from wallet.models import Wallet, currencies, Settings, GroupMember


class TransferForm(forms.Form):
	amount=forms.DecimalField(min_value=0,decimal_places=2,label='',
		widget=forms.NumberInput(attrs={'placeholder':'Transfer Amount'}))
	currency=forms.ChoiceField(currencies,label='')
	user=forms.IntegerField(label='',
		widget=forms.NumberInput(attrs={'placeholder':"Enter recipient's id"}))

class ForexForm(forms.Form):
	amount=forms.DecimalField(min_value=1,decimal_places=2,label='',
		widget=forms.NumberInput(attrs={'placeholder':'Exchange Amount'}))
	currency_have=forms.ChoiceField(currencies,label='')
	currency_want=forms.ChoiceField(currencies,label='')

class SettingsForm(forms.ModelForm):
	class Meta:
		model=Settings
		fields=['borrow_lend']
	
			

class GroupForm(forms.Form):
	def __init__(self,user,*args,**kwargs):
		super(SettingsForm,self).__init__(*args,**kwargs)
		self.fields['groups'] = forms.ChoiceField(
			choices=[(o.id,str(o)) for o in GroupMember.objects.filter(person=user)])