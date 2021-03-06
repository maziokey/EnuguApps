# Generated by Django 2.0 on 2017-12-15 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_index=True, max_length=31)),
                ('last_name', models.CharField(db_index=True, max_length=31)),
                ('passport_number', models.CharField(db_index=True, max_length=10)),
                ('form_number', models.CharField(db_index=True, max_length=10)),
                ('sticker_number', models.CharField(db_index=True, max_length=10)),
                ('extension_period', models.CharField(max_length=8)),
                ('purchase_date', models.DateField(verbose_name='date of purchase')),
                ('slug', models.SlugField(help_text='A label for URL config.', max_length=31, unique=True)),
            ],
            options={
                'get_latest_by': 'purchase_date',
                'ordering': ['form_number'],
            },
        ),
    ]
