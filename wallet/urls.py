from django.conf.urls import url
from wallet import views

urlpatterns=[
	url(r'',views.wallet_summary,name="wallet_summary"),
	url(r'^transfer/$',views.transfer,name='transfer'),
	url(r'^info/$',views.info,name='info'),
	url(r'^activity/$',views.RecentActivityView.as_view(),name='activity')

]