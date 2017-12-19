from django import forms
from django.forms.widgets import HiddenInput
from django.core.exceptions import ValidationError

from .models import Applicant

class SlugCleanMixin:
    """Mixin class for slug cleaning method."""

    def clean_slug(self):
        new_slug = (self.cleaned_data['slug'].lower())
        if new_slug == 'create':
            raise ValidationError('Slug may not be "create".')
        return new_slug

class ApplicantForm(SlugCleanMixin, forms.ModelForm):
	class Meta:
		model = Applicant
		fields = '__all__'