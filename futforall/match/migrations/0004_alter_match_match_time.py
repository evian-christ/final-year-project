# Generated by Django 4.1.3 on 2022-11-24 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0003_match_match_time_alter_match_match_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='match_time',
            field=models.TimeField(default='00:00'),
        ),
    ]
