# Generated by Django 3.1.2 on 2020-11-11 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('review', '0001_initial'),
        ('user', '0001_initial'),
        ('stay', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='guest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
        migrations.AddField(
            model_name='review',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.host'),
        ),
        migrations.AddField(
            model_name='review',
            name='stay',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stay.stay'),
        ),
    ]
