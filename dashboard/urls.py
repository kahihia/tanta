from django.conf.urls import url
from dashboard import views

app_name='dashboard'

urlpatterns=[ 
url(r'^dashboard/logout',views.user_logout,name='logout'),
url(r'^',views.home,name="home")

]