# Generated by Django 3.0.4 on 2020-06-27 07:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('devcamper_api', '0006_reviews'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bootcamps',
            new_name='Bootcamp',
        ),
        migrations.RenameModel(
            old_name='Courses',
            new_name='Course',
        ),
        migrations.RenameModel(
            old_name='Reviews',
            new_name='Review',
        ),
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]
