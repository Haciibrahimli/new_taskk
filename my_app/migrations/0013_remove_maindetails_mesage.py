# Generated by Django 4.2.5 on 2023-11-01 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0012_maindetails_map_url_alter_maindetails_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maindetails',
            name='mesage',
        ),
    ]
