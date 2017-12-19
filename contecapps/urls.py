"""contecapps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView
#from django.urls import path

from epass import urls as epass_urls

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='epass_applicant_list', permanent=False)),
    #path('admin/', admin.site.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^epass/', include(epass_urls)),
]
