# Generated by Django 2.0 on 2018-01-28 17:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('epass', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='Added_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='epass_applicants', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
