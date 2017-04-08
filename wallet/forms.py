from django import forms
from django.core import validators

class TransferForm(forms.Form):
	amount=forms.DecimalField(max_digits=7,decimal_places=2,min_value=0)
	user=forms.IntegerField()