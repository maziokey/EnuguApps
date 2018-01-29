from django.conf.urls import url
from django.urls import path
from django_filters.views import FilterView
from .views import home, ApplicantCreate, ApplicantDelete, ApplicantUpdate, ApplicantList, ApplicantDetail
from .filters import ApplicantFilter

urlpatterns = [
    path('', home, name='home'),
    url(r'^applicants/$', ApplicantList.as_view(), name='epass_applicant_list'),
    #url(r'^$', ApplicantList.as_view(), name='epass_applicant_list'),
    url(r'^search/$', FilterView.as_view(filterset_class=ApplicantFilter, template_name='epass/search_list.html'), name='epass_search'),
    url(r'^create/$', ApplicantCreate.as_view(), name='epass_applicant_create'),
    url(r'^(?P<slug>[\w\-]+)/$', ApplicantDetail.as_view(), name='epass_applicant_detail'),
    url(r'^(?P<slug>[\w\-]+)/delete/$', ApplicantDelete.as_view(), name='epass_applicant_delete'),
    url(r'^(?P<slug>[\w\-]+)/update/$', ApplicantUpdate.as_view(), name='epass_applicant_update'),
]