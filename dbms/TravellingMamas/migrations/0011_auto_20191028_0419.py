# Generated by Django 2.2 on 2019-10-27 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TravellingMamas', '0010_auto_20191028_0007'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_hotel_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('room_type', models.CharField(max_length=100)),
                ('hotel_name', models.CharField(max_length=100)),
                ('check_in', models.CharField(max_length=100)),
                ('check_out', models.CharField(max_length=100)),
                ('number_of_guests', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=100)),
                ('user_id', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='user_details',
        ),
    ]
