from django.db import models
#from django.core.urlresolvers import reverse (old version of django)
from django.urls import reverse

# Create your models here.
class Applicant(models.Model):
	first_name = models.CharField(max_length=31, db_index=True)
	last_name = models.CharField(max_length=31, db_index=True)
	passport_number = models.CharField(max_length=10, db_index=True)
	form_number = models.CharField(max_length=10, db_index=True)
	sticker_number = models.CharField(max_length=10, db_index=True)
	extension_period = models.CharField(max_length=8)
	purchase_date = models.DateField('date of purchase')
	slug = models.SlugField(max_length=31, unique=True, help_text='A label for URL config.')

	def __str__(self):
		return self.form_number

	def get_absolute_url(self):
		return reverse('epass_applicant_detail', kwargs={'slug': self.slug})

	def get_update_url(self):
		return reverse('epass_applicant_update', kwargs={'slug': self.slug})

	def get_delete_url(self):
		return reverse('epass_applicant_delete', kwargs={'slug': self.slug})

	class Meta:
		ordering = ['form_number']
		get_latest_by = 'purchase_date'
