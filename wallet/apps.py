from django.apps import AppConfig

class WalletConfig(AppConfig):
    name = 'wallet'

    def ready(self):
    	from actstream import registry
    	registry.register(self.get_model('Wallet'))
    	registry.register(self.get_model('Transactions'))
    # 	# registry.register(self.get_model('User'))
