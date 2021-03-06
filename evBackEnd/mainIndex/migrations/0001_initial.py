# Generated by Django 4.0.4 on 2022-06-04 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='chargerState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charger_state', models.BooleanField(default=0)),
                ('charger_mode', models.IntegerField(default=1)),
                ('ev_connect_state', models.BooleanField(default=0)),
                ('update_time', models.TimeField(null=True)),
                ('update_date', models.DateField(null=True)),
            ],
        ),
    ]
