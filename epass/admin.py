from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from import_export import fields, resources
from django.contrib import admin
from .models import Applicant
from django.contrib.auth.models import User

# Register your models here.
class ApplicantResource(resources.ModelResource):
    id = fields.Field(column_name='id', attribute='id')
    first_name = fields.Field(column_name='first_name', attribute='first_name')
    last_name = fields.Field(column_name='last_name', attribute='last_name')
    passport_number = fields.Field(column_name='passport_number', attribute='passport_number')
    form_number = fields.Field(column_name='form_number', attribute='form_number')
    sticker_number = fields.Field(column_name='sticker_number', attribute='sticker_number')
    extension_period = fields.Field(column_name='extension_period', attribute='extension_period')
    purchase_date = fields.Field(column_name='purchase_date', attribute='purchase_date')
    slug = fields.Field(column_name='slug', attribute='slug')
    Added_by = fields.Field(column_name='Added_by', attribute='Added_by', widget=ForeignKeyWidget(User, 'username'))

    class Meta:
        model = Applicant
        skip_unchanged = True
        fields = ('first_name', 'last_name', 'passport_number', 'form_number', 'sticker_number', 'extension_period', 'purchase_date', 'slug', 'Added_by', )


class ApplicantAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('form_number', 'first_name', 'last_name', 'passport_number', 'sticker_number', 'Added_by')
    list_filter = ('purchase_date',)
    search_fields = ('form_number', 'passport_number', 'sticker_number')
    prepopulated_fields = {'slug': ('form_number',)}
    date_hierarchy = 'purchase_date'
    ordering = ['purchase_date']
    resource_class = ApplicantResource

admin.site.register(Applicant, ApplicantAdmin)
