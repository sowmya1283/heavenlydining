# Generated by Django 4.2.23 on 2025-07-02 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktable', '0003_alter_booking_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='username',
        ),
    ]
