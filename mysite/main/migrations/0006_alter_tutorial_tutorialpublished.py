# Generated by Django 4.0.4 on 2022-06-17 12:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_tutorial_tutorialpublished'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorialPublished',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 17, 14, 55, 32, 598673), verbose_name='date published'),
        ),
    ]
