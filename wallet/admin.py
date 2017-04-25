from django.contrib import admin

from wallet.models import Wallet,Transactions,ForexRates,Group,GroupMember,Contacts,Settings,Social
# Register your models here.
admin.site.register(Wallet)
admin.site.register(Transactions)
admin.site.register(ForexRates)
admin.site.register(Group)
admin.site.register(GroupMember)
admin.site.register(Contacts)
admin.site.register(Settings)
admin.site.register(Social)