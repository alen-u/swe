# Generated by Django 4.1.4 on 2023-03-03 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_anonymoustip_incident_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anonymoustip',
            name='stay_in_touch',
        ),
    ]
