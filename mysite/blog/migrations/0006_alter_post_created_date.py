# Generated by Django 4.1 on 2023-05-12 01:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 12, 1, 43, 5, 365784, tzinfo=datetime.timezone.utc)),
        ),
    ]
