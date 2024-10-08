# Generated by Django 4.1 on 2024-07-21 18:50

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to.', related_name='myuser_set', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='myuser_set', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.SmallIntegerField(choices=[(0, 'Mr'), (1, 'Mrs'), (2, 'Miss')])),
                ('field', models.CharField(max_length=50)),
                ('due_date', models.DateTimeField(default=datetime.datetime(2024, 7, 21, 18, 49, 59, 819317, tzinfo=datetime.timezone.utc))),
                ('qualifications', models.TextField(max_length=100)),
                ('institution', models.TextField(max_length=100)),
                ('status', models.BooleanField(default=True)),
                ('first_name', models.OneToOneField(db_column='tutor_first_name', on_delete=django.db.models.deletion.CASCADE, related_name='tutor_first_name', to=settings.AUTH_USER_MODEL)),
                ('last_name', models.OneToOneField(db_column='tutor_last_name', on_delete=django.db.models.deletion.CASCADE, related_name='tutor_last_name', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.SmallIntegerField(choices=[(0, 'Mr'), (1, 'Mrs'), (2, 'Miss')])),
                ('service_type', models.SmallIntegerField(choices=[(0, 'Research ass'), (1, 'Professor'), (2, 'Doctor'), (3, 'Masters')])),
                ('field', models.CharField(max_length=50)),
                ('due_date', models.DateTimeField(default=datetime.datetime(2024, 7, 21, 18, 49, 59, 816419, tzinfo=datetime.timezone.utc))),
                ('description', models.TextField(max_length=285)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 7, 21, 18, 49, 59, 816531, tzinfo=datetime.timezone.utc))),
                ('status', models.BooleanField(default=True)),
                ('first_name', models.OneToOneField(db_column='student_first_name', on_delete=django.db.models.deletion.CASCADE, related_name='student_first_name', to=settings.AUTH_USER_MODEL)),
                ('last_name', models.OneToOneField(db_column='student_last_name', on_delete=django.db.models.deletion.CASCADE, related_name='student_last_name', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.SmallIntegerField(choices=[(0, 'Research ass'), (1, 'Professor'), (2, 'Doctor'), (3, 'Masters')])),
                ('field', models.CharField(max_length=50)),
                ('due_date', models.DateTimeField(default=datetime.datetime(2024, 7, 28, 18, 49, 59, 821967, tzinfo=datetime.timezone.utc))),
                ('file_name', models.CharField(max_length=60)),
                ('file', models.FileField(null=True, upload_to='Documents/')),
                ('description', models.TextField()),
                ('created', models.DateTimeField(default=datetime.datetime(2024, 7, 21, 18, 49, 59, 822172, tzinfo=datetime.timezone.utc))),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='service_matcher.student')),
                ('tutor', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='service_matcher.tutor')),
            ],
        ),
    ]
