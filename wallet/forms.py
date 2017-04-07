from django import forms
from wallet.models import Wallet

class TransferForm(forms.Form):
	amount=forms.DecimalField(max_digits=5,decimal_places=2,min_value=0)
