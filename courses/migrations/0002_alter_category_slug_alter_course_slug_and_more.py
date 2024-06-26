# Generated by Django 5.0.6 on 2024-05-20 18:25

import django_extensions.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, overwrite=True, populate_from='name', unique=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, overwrite=True, populate_from='title', unique=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, overwrite=True, populate_from='title', unique=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, overwrite=True, populate_from='title', unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, overwrite=True, populate_from='first_name', unique=True),
        ),
        migrations.AlterField(
            model_name='studentsubmission',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, overwrite=True, populate_from='title', unique=True),
        ),
    ]
