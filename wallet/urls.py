from django.conf.urls import url
from wallet import views

urlpatterns=[
	url(r'^$',views.wallet_summary,name="wallet_summary"),
	url(r'^transfer/$',views.transfer,name='transfer'),
	url(r'^info/$',views.info,name='info'),
	url(r'^forex/$',views.forex,name='forex'),
	url(r'^settings/$',views.settings,name='settings'),
	url(r'^contacts/$',views.contacts,name='contacts'),
	url(r'^peer2peer/$',views.p2p,name='p2p'),
	url(r'^groups/$',views.groups,name='groups'),
	url(r'^contacts/add/$',views.add_contacts,name='add_contact'),
	url(r'^info/reset/$',views.passreset,name='pword'),
	url(r'^groups/display_groups/$',views.display_groups,name='display_groups'),
	url(r'^contacts/verify/$',views.send_contacts,name='verify_contact'),
	url(r'^groups/group_limit/$',views.group_limit,name='group_limit'),
	url(r'^groups/remove/$',views.group_remove,name='group_remove'),

]