# Generated by Django 3.2.15 on 2022-08-27 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myspace', '0005_auto_20220827_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='office_spaces_booked',
            name='end_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='office_spaces_booked',
            name='start_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
