# Generated by Django 4.0 on 2022-01-31 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notificationtext', models.CharField(max_length=200)),
                ('notificationdate', models.CharField(max_length=30)),
            ],
        ),
    ]
