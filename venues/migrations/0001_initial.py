# Generated by Django 3.0.2 on 2020-04-13 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('code', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'building',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('code', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('floor', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venues.Building')),
            ],
            options={
                'db_table': 'room',
            },
        ),
    ]
