# Generated by Django 5.1.6 on 2025-03-19 19:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_matching', '0002_alter_jobmatchanalysis_table'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobmatchanalysis',
            name='keyword_matches',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='jobmatchanalysis',
            name='matched_skills',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='jobmatchanalysis',
            name='missing_skills',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='jobmatchanalysis',
            name='suggestions',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='jobmatchanalysis',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
