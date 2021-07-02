# Generated by Django 3.2.4 on 2021-07-01 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='rcdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=11)),
                ('State', models.CharField(max_length=15)),
                ('City', models.CharField(max_length=15)),
                ('Site', models.CharField(max_length=15)),
                ('Material', models.CharField(max_length=15)),
                ('Weight_g', models.FloatField()),
                ('Laboratory', models.CharField(max_length=15)),
                ('LabID', models.CharField(max_length=15)),
                ('Age_BP', models.IntegerField()),
                ('Error', models.IntegerField()),
                ('Report', models.TextField()),
            ],
        ),
    ]