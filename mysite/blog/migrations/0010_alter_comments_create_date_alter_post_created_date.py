# Generated by Django 4.1 on 2023-05-15 14:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_comments_create_date_alter_post_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 15, 20, 19, 7, 511969, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 15, 20, 19, 7, 511969, tzinfo=datetime.timezone.utc)),
        ),
    ]