# Generated by Django 4.1 on 2024-07-29 20:34

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service_matcher', '0002_remove_student_user_remove_tutor_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 29, 20, 34, 12, 595466, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='document',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 5, 20, 34, 12, 595268, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='document',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service_matcher.student'),
        ),
        migrations.AlterField(
            model_name='document',
            name='tutor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='service_matcher.tutor'),
        ),
        migrations.AlterField(
            model_name='student',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 29, 20, 34, 12, 587129, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='student',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 29, 20, 34, 12, 586715, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 29, 20, 34, 12, 593103, tzinfo=datetime.timezone.utc)),
        ),
    ]
