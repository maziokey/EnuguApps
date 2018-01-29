from django.contrib import admin
from .models import Applicant

# Register your models here.
class ApplicantAdmin(admin.ModelAdmin):
	list_display = ('form_number', 'first_name', 'last_name', 'passport_number', 'sticker_number', 'Added_by')
	list_filter = ('purchase_date',)
	search_fields = ('form_number', 'passport_number', 'sticker_number')
	prepopulated_fields = {'slug': ('form_number',)}
	date_hierarchy = 'purchase_date'
	ordering = ['purchase_date']

admin.site.register(Applicant, ApplicantAdmin)