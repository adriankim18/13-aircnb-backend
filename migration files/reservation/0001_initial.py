# Generated by Django 3.1.2 on 2020-11-09 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin_date', models.DateField()),
                ('checkout_date', models.DateField()),
                ('guest_number', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=60)),
                ('creditcard', models.CharField(max_length=200)),
                ('request_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'bookings',
            },
        ),
        migrations.CreateModel(
            name='Cancellation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cancel_date', models.DateTimeField(auto_now_add=True)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.booking')),
            ],
            options={
                'db_table': 'cancellations',
            },
        ),
    ]