# Generated by Django 4.1 on 2024-10-03 20:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_matcher', '0003_alter_document_created_alter_document_due_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 3, 20, 26, 27, 264767, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='document',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 10, 20, 26, 27, 264565, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='student',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 3, 20, 26, 27, 259602, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='student',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 3, 20, 26, 27, 259489, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 3, 20, 26, 27, 262312, tzinfo=datetime.timezone.utc)),
        ),
    ]
