from django import forms
from wallet.models import Wallet

class TransferForm(forms.Form):
	amount=forms.DecimalField(max_digits=7,decimal_places=2,min_value=0,label='',
		widget=forms.NumberInput(attrs={'placeholder':'Transfer Amount'}))
	user=forms.IntegerField(label='',
		widget=forms.NumberInput(attrs={'placeholder':"Enter recipient's id"}))
	currency=forms.ChoiceField(choices=[('USD','GBP','EUR','GHC')])