# Generated by Django 3.2.15 on 2022-08-27 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myspace', '0002_auto_20220827_1917'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meeting_rooms_booked',
            options={'ordering': ['created_on']},
        ),
        migrations.AlterModelOptions(
            name='office_spaces_booked',
            options={'ordering': ['created_on']},
        ),
    ]
