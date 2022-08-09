# Generated by Django 4.0.5 on 2022-07-28 18:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('executor', '0003_executorcomments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='executor',
            name='phone_number',
            field=models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(regex='^\\+375\\d{9}$')]),
        ),
        migrations.AlterField(
            model_name='executor',
            name='photo',
            field=models.URLField(blank=True),
        ),
    ]
