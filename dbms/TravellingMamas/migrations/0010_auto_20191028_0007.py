# Generated by Django 2.2 on 2019-10-27 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TravellingMamas', '0009_flight_prime_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_flight_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_city', models.CharField(max_length=100)),
                ('destination_city', models.CharField(max_length=100)),
                ('airline', models.CharField(max_length=100)),
                ('seat_type', models.CharField(max_length=100)),
                ('departure_date', models.CharField(max_length=100)),
                ('adult_count', models.CharField(max_length=100)),
                ('child_count', models.CharField(max_length=100)),
                ('fullname', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('user_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='user_details',
            name='user_id',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
