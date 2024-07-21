from django.db import models
from django.contrib.auth.models import (User, UserManager,AbstractBaseUser,
                                         BaseUserManager, PermissionsMixin)
from datetime import datetime, timedelta
from django.utils import timezone

# Create your models here.


TITLE_CHOICES = (
     (0,'Mr'),
     (1,'Mrs'),
     (2,'Miss'),
)
SERVICE_TYPE = (
     (0,'Research ass'),
     (1,'Professor'),
     (2,'Doctor'),
     (3,'Masters'),
)


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='myuser_set',  # Avoid clashes with the default User model
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )


    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='myuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.email


class Student(models.Model):
      
        title = models.SmallIntegerField(choices=TITLE_CHOICES)
        first_name = models.OneToOneField(MyUser,related_name='student_first_name', db_column='student_first_name',on_delete=models.CASCADE)
        last_name = models.OneToOneField(MyUser, related_name='student_last_name', db_column='student_last_name',on_delete=models.CASCADE)
        service_type = models.SmallIntegerField(choices=SERVICE_TYPE)
        field = models.CharField(max_length=50, blank=False)
        due_date = models.DateTimeField(default=timezone.now())
        description = models.TextField(max_length=285)
        created_at =  models.DateTimeField(default=timezone.now())
        status  = models.BooleanField(default=True)

        def __str__(self):
             return   {f"{self.title}+ {self.first_name} + {self.last_name} + {self.field}"}
        

class Tutor(models.Model):
        
        title = models.SmallIntegerField(choices=TITLE_CHOICES)
        first_name = models.OneToOneField(MyUser,related_name='tutor_first_name', db_column='tutor_first_name',on_delete=models.CASCADE)
        last_name = models.OneToOneField(MyUser,related_name='tutor_last_name', db_column='tutor_last_name',on_delete=models.CASCADE)
        field = models.CharField(max_length=50, blank=False)
        due_date = models.DateTimeField(default= timezone.now())
        qualifications = models.TextField(max_length=100)
        institution = models.TextField(max_length=100)
        status  = models.BooleanField(default=True)

        
        def __str__(self):
              return   {f"{self.title} {self.first_name}{self.last_name}{self.field}"}
class Document(models.Model):
     
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, blank=True, null=True, on_delete=models.SET_NULL)
    service_type = models.SmallIntegerField(choices=SERVICE_TYPE)
    field = models.CharField(max_length=50)
    due_date = models.DateTimeField(default=timezone.now() + timedelta(weeks=1))
    file_name = models.CharField(max_length=60, blank=False, null=False)
    file = models.FileField(upload_to='Documents/',null=True)
    description = models.TextField()
    created = models.DateTimeField(default=timezone.now())

    # def __str__(self):
    #     return {f"{self.student}"}