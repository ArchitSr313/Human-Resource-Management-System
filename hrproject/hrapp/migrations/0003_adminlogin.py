# Generated by Django 4.0 on 2022-01-25 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrapp', '0002_jobseeker'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminLogin',
            fields=[
                ('userid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
