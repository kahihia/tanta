"""Tanta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from home_page import views
from dashboard import views
from community import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views

urlpatterns =[
    url(r'^admin/', admin.site.urls),
    url(r'^',include("home_page.urls",namespace='home_page')),
    url(r'^dashboard/',include("dashboard.urls",namespace='dashboard')),
    # url(r'^community/',include("community.urls",namespace="community")),
    url(r'^accounts/login/$',views.login,name='login'),
    url(r'^accounts/logout/$',views.logout,name='logout',kwargs={'next_page':'/'}),
    url(r'^tantapay/',include("wallet.urls",namespace="wallet")),
    # url(r'^activity/',include('actstream.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)