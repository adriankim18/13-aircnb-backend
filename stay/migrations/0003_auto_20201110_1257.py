# Generated by Django 3.1.2 on 2020-11-10 12:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stay', '0002_auto_20201109_2318'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stay',
            old_name='address',
            new_name='address1',
        ),
        migrations.RenameField(
            model_name='stay',
            old_name='monthly_price',
            new_name='discount_price',
        ),
        migrations.RemoveField(
            model_name='houserule',
            name='title',
        ),
        migrations.AddField(
            model_name='stay',
            name='address2',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
    ]
