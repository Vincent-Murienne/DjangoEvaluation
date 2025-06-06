# Generated by Django 5.2.1 on 2025-05-28 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_id', models.AutoField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=100)),
                ('last_update', models.DateField()),
                ('capital', models.BooleanField(default=False)),
                ('picture', models.BinaryField(blank=True, null=True)),
            ],
            options={
                'db_table': 'city',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country_id', models.AutoField(primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=100)),
                ('last_update', models.DateField()),
            ],
            options={
                'db_table': 'country',
                'managed': False,
            },
        ),
    ]
