# Generated by Django 3.2.15 on 2022-08-27 19:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myspace', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting_Rooms_Booked',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('status', models.IntegerField(choices=[(0, 'Open'), (1, 'Booked'), (2, 'Cancelled')], default=1)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Office_Spaces_Booked',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('status', models.IntegerField(choices=[(0, 'Open'), (1, 'Booked'), (2, 'Cancelled')], default=1)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='status',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='ID',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='meeting_rooms',
            old_name='ID',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='office_spaces',
            old_name='ID',
            new_name='id',
        ),
        migrations.AddField(
            model_name='office_spaces_booked',
            name='Office_Space_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myspace.office_spaces'),
        ),
        migrations.AddField(
            model_name='office_spaces_booked',
            name='category_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myspace.category'),
        ),
        migrations.AddField(
            model_name='office_spaces_booked',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='meeting_rooms_booked',
            name='category_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myspace.category'),
        ),
        migrations.AddField(
            model_name='meeting_rooms_booked',
            name='meeting_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myspace.meeting_rooms'),
        ),
        migrations.AddField(
            model_name='meeting_rooms_booked',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]