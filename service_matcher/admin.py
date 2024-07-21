from django.contrib import admin
from .models import MyUser, Student,Tutor,  Document
# Register your models here.
admin.site.register(MyUser),
admin.site.register(Student),
admin.site.register(Tutor),
admin.site.register(Document),