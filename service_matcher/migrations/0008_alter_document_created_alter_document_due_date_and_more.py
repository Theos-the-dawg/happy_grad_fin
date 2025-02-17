# Generated by Django 4.1 on 2024-10-17 17:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_matcher', '0007_alter_document_created_alter_document_due_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 17, 17, 48, 5, 242156, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='document',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 24, 17, 48, 5, 241957, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='student',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 17, 17, 48, 5, 236890, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='student',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 17, 17, 48, 5, 236712, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 17, 17, 48, 5, 239619, tzinfo=datetime.timezone.utc)),
        ),
    ]
