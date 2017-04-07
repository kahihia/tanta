from django import forms
from wallet.models import Wallet

class TransferForm(forms.ModelForm):
	balance=forms.DecimalField(max_digits=5,decimal_places=2)
	class Meta():
		model=Wallet
		fields=['balance']
	