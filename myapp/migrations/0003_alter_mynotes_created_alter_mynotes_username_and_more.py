# Generated by Django 4.1.3 on 2023-01-02 09:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_mynotes_alter_usersignup_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mynotes',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 2, 14, 50, 8, 837034)),
        ),
        migrations.AlterField(
            model_name='mynotes',
            name='username',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='usersignup',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 2, 14, 50, 8, 837034)),
        ),
    ]
