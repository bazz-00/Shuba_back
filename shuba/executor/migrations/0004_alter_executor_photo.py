# Generated by Django 4.0.5 on 2022-07-26 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('executor', '0003_executorcomments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='executor',
            name='photo',
            field=models.URLField(blank=True),
        ),
    ]