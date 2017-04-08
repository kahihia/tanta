from django import forms
from wallet.models import Wallet

balance=Wallet.balance
class TransferForm(forms.Form):
	amount=forms.DecimalField(max_digits=7,decimal_places=2,min_value=0)
	user=forms.IntegerField()