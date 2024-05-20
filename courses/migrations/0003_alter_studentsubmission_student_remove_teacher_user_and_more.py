# Generated by Django 5.0.6 on 2024-05-20 20:56

import django.db.models.deletion
import django_extensions.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_category_slug_alter_course_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsubmission',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.profile'),
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='user',
        ),
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_teacher',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(related_name='enrolled_students', to='courses.profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, overwrite=True, populate_from=('first_name', 'last_name'), unique=True),
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
