# Generated by Django 4.2.3 on 2023-08-01 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_id', models.CharField(max_length=100)),
                ('date_and_time', models.CharField(max_length=100)),
                ('subscriber_count', models.CharField(max_length=100)),
                ('view_count', models.CharField(max_length=100)),
                ('video_count', models.CharField(max_length=100)),
            ],
        ),
    ]
