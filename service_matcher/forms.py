from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser, Student,Tutor,TITLE_CHOICES,SERVICE_TYPE,Document


# class StudentSignUpForm(UserCreationForm):
#     title = forms.ChoiceField(choices=TITLE_CHOICES)
#     service_type = forms.ChoiceField(choices=SERVICE_TYPE)
#     field = forms.CharField(max_length=50)
#     due_date = forms.DateTimeField()
#     description = forms.CharField(widget=forms.Textarea, max_length=285)

#     class Meta:
#         model = MyUser
#         fields = ('email', 'first_name', 'last_name', 'password1', 'password2')

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         if commit:
#             user.save()
#             Student.objects.create(
#                 first_name=user,
#                 last_name=user,
#                 title=self.cleaned_data['title'],
#                 service_type=self.cleaned_data['service_type'],
#                 field=self.cleaned_data['field'],
#                 due_date=self.cleaned_data['due_date'],
#                 description=self.cleaned_data['description']
#             )
#         return user

        
# class TutorSignUpForm(UserCreationForm):
#     title = forms.ChoiceField(choices=TITLE_CHOICES)
#     service_type = forms.ChoiceField(choices=SERVICE_TYPE)
#     field = forms.CharField(max_length=50)
#     due_date = forms.DateTimeField()
#     qualifications = forms.CharField(max_length=50)
#     institution = forms.CharField(max_length=50)
    

#     class Meta:
#         model = MyUser
#         fields = ('email', 'first_name', 'last_name', 'password1', 'password2')

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         if commit:
#             user.save()
#             Tutor.objects.create(
#                 first_name=user,
#                 last_name=user,
#                 title=self.cleaned_data['title'],
#                 service_type=self.cleaned_data['service_type'],
#                 field=self.cleaned_data['field'],
#                 due_date=self.cleaned_data['due_date'],
#                 qualifications=self.cleaned_data['qualifications'],
#                 institution =self.cleaned_data['institution'],
#             )
#         return user
    
class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), label="")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}), label="")


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['service_type', 'field', 'due_date', 'file_name', 'file', 'description']


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ['email', 'first_name', 'last_name', 'password']

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['title', 'service_type', 'field', 'description']

class TutorRegistrationForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ['title',  'field', 'qualifications', 'institution']
