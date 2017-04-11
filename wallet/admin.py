from django.contrib import admin

from wallet.models import Wallet,Transactions
# Register your models here.
admin.site.register(Wallet)
admin.site.register(Transactions)