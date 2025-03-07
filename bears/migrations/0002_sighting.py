# Generated by Django 5.1.6 on 2025-02-28 17:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bears', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sighting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deploy_id', models.IntegerField(default=None)),
                ('recieved', models.TextField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('temperature', models.FloatField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('bear_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sightings', to='bears.bear')),
            ],
        ),
    ]
