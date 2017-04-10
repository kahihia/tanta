from django import forms
from wallet.models import Wallet, currencies


class TransferForm(forms.Form):
	amount=forms.DecimalField(max_digits=7,decimal_places=2,min_value=0,label='',
		widget=forms.NumberInput(attrs={'placeholder':'Transfer Amount'}))
	currency=forms.ChoiceField(currencies,label='')
	user=forms.IntegerField(label='',
		widget=forms.NumberInput(attrs={'placeholder':"Enter recipient's id"}))
