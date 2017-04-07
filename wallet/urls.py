from django.conf.urls import url
from wallet import views

urlpatterns=[
	url(r'',views.wallet_summary,name="wallet_home"),

]