from django.conf.urls import url
from wallet import views

urlpatterns=[
	url(r'^$',views.wallet_summary,name="wallet_summary"),
	url(r'^transfer/$',views.transfer,name='transfer'),
	url(r'^info/$',views.info,name='info'),
	url(r'^forex/$',views.forex,name='forex'),
	url(r'^settings/$',views.settings,name='settings'),
	url(r'^contacts/$',views.contacts,name='contacts'),

]