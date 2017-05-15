from django.conf.urls import url
from peer2peer import views

urlpatterns=[
	url(r'^$',views.p2p,name='p2phome'),
]