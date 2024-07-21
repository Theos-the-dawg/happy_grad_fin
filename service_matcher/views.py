from pyexpat.errors import messages
from django.shortcuts import redirect, render
from .forms import LoginForm, StudentRegistrationForm,TutorRegistrationForm
from django.contrib.auth import authenticate, login as auth_login,logout
from .forms import DocumentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .forms import UserRegistrationForm, StudentRegistrationForm, TutorRegistrationForm
from .models import Student, Tutor


def home(request):
    return render(request,'home.html')

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            # Check if the student exists
            try:
                student = Student.objects.get(first_name__email=email)
            except Student.DoesNotExist:
                student = None

            if student is not None:
                # Authenticate the student
                authenticated_student = authenticate(request, email=email, password=password)
                if authenticated_student is not None:
                    auth_login(request, authenticated_student)
                    return redirect('services')
                else:
                    messages.error(request, 'Invalid email or password.')

            else:
                # Check if the tutor exists
                try:
                    tutor = Tutor.objects.get(first_name__email=email)
                except Tutor.DoesNotExist:
                    tutor = None

                if tutor is not None:
                    # Authenticate the tutor
                    authenticated_tutor = authenticate(request, email=email, password=password)
                    if authenticated_tutor is not None:
                        auth_login(request, authenticated_tutor)
                        return redirect('services')
                    else:
                        messages.error(request, 'Invalid email or password.')
                else:
                    messages.error(request, 'User does not exist.')

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')   
    
"""works just needs a bit of cleaning and exception handling """
def create_Student(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        student_form = StudentRegistrationForm(request.POST)
        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            student = student_form.save(commit=False)
            student.first_name = user
            student.last_name = user
            student.save()
            authenticated_user = authenticate(email=user.email, password=user_form.cleaned_data['password'])
            auth_login(request, authenticated_user)
            return redirect('services')
    else:
        user_form = UserRegistrationForm()
        student_form = StudentRegistrationForm()
    return render(request, 'create_student.html', {'user_form': user_form, 'student_form': student_form})

"""works just needs a bit of cleaning and exception handling """
def create_Tutor(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        tutor_form = TutorRegistrationForm(request.POST)
        if user_form.is_valid() and tutor_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            tutor = tutor_form.save(commit=False)
            tutor.first_name = user
            tutor.last_name = user
            tutor.save()
            authenticated_user = authenticate(email=user.email, password=user_form.cleaned_data['password'])
            auth_login(request, authenticated_user)
            return redirect('services')
    else:
        user_form = UserRegistrationForm()
        tutor_form = TutorRegistrationForm()
    return render(request, 'create_tutor.html', {'user_form': user_form, 'tutor_form': tutor_form})

def services(request):
    return render(request,'services.html')

def useful_links(request):
    return render(request,'useful_links.html')

def join_the_team(request):
    return render(request, 'join_the_team.html')
@login_required  #alt for currrent logic
def documents(request):
    form = DocumentForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, 'You need to be logged in to submit a request.')
            return redirect('login')

        # if not hasattr(request.user, 'student'):
        #     messages.error(request, 'Only students can submit a document request.')
        #     return redirect('home')
        print(form)
    if form.is_valid():
        document = form.save(commit=False)
        student = Student.objects.get(user=request.user)  # Assuming there's a relationship between User and Student
        document.student = student
       

        document.save()
        messages.success(request, 'Your request has been submitted.')
        return redirect('home')

    return render(request, 'documents.html', {'form': form})
    