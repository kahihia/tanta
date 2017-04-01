from django.conf.urls import url
from home_page import views

app_name='home_page'

urlpatterns=[
	url(r'^$',views.index,name='index'),
	url(r'contact/$',views.contact,name='contact'),
	url(r'^about/$',views.about,name='about'),
	url(r'^onyx/$',views.onyx,name='onyx'),
	url(r'^getstarted/$',views.getstarted,name='getstart'),
	url(r'^sign_in/',views.signin,name='sign_in'),
	url(r'^logout/$',views.user_logout,name='logout')
]