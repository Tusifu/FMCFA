# Generated by Django 3.0.7 on 2020-11-29 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HospitalAgent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('age', models.IntegerField()),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('dob', models.DateTimeField()),
            ],
            options={
                'db_table': 'HospitalAgent',
            },
        ),
        migrations.CreateModel(
            name='Pharmacist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('age', models.IntegerField()),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('dob', models.DateTimeField()),
            ],
            options={
                'db_table': 'Pharmacist',
            },
        ),
    ]
