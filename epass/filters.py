from django import forms
from .models import Applicant
import django_filters

class ApplicantFilter(django_filters.FilterSet):
	first_name = django_filters.CharFilter(lookup_expr='icontains')
	last_name = django_filters.CharFilter(lookup_expr='icontains')
	purchase_date = django_filters.NumberFilter(name='purchase_date', lookup_expr='month')

	class Meta:
		model = Applicant
		fields = {
		    'first_name': ['icontains', ],
		    'last_name': ['icontains', ],
		    'purchase_date': ['month', ],
		    'passport_number': ['exact', ],
		    'form_number': ['exact', ],
		    'sticker_number': ['exact', ],
		}