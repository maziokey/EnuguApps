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
from django.views.generic import RedirectView, TemplateView
from django.urls import path

from epass import urls as epass_urls
from contact import urls as contact_urls
#from epass.views import home

urlpatterns = [
    #url(r'^$', RedirectView.as_view(pattern_name='epass_applicant_list', permanent=False)),
    url(r'^$', RedirectView.as_view(pattern_name='home', permanent=False)),
    #path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^about/$', TemplateView.as_view(template_name='site/about.html'), name='about_site'),
    #path('admin/', admin.site.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^epass/', include(epass_urls)),
    url(r'^contact/', include(contact_urls)),
]
