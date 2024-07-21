from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import MyUser,Student,Tutor
from .forms import LoginForm, StudentSignUpForm,TutorSignUpForm
from django.contrib.auth import authenticate, login,logout
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Document
from .forms import DocumentForm
from django.contrib.auth.decorators import login_required

"""This is a page dedicated for the code options for logic flow"""

def login(request):
    if not hasattr(request.user, 'student'):
            messages.error(request, 'Only students can create a document request.')
            return redirect('home')

    form = DocumentForm(request.POST or None, request.FILES or None)
    if form.is_valid():
            document = form.save(commit=False)
            document.student = request.user.student
            document.save()
            messages.success(request, 'Your request has been submitted.')
            return redirect('home')

    return render(request, 'login.html', {'form': form})
#def login(request):
# form = LoginForm(request.POST or None)
    # if request.method == 'POST':
    #         if form.is_valid():
    #             email = form.cleaned_data.get('email')
    #             password = form.cleaned_data.get('password')
                
    #             # Check if the student exists
    #             try:
    #                 student = Student.objects.get(email=email)
    #             except Student.DoesNotExist:
    #                 student = None
    #                  # Check if the tutor exists
    #             if student is None :
    #                 try:
    #                     tutor = Tutor.objects.get(email=email)
    #                 except Tutor.DoesNotExist:
    #                     tutor = None
                    
    #                 if tutor is not None:
    #                     # Authenticate the student
    #                     authenticated_tutor = authenticate(request, email=email, password=password)
    #                     if authenticated_tutor is not None:
    #                         login(request, authenticated_tutor)
    #                         return redirect(reverse('services'))
    #                     else:
    #                         messages.error(request, 'Invalid email or password.')
    #                 else:
    #                     messages.error(request, 'tutor does not exist.')    
                
    #             if student is not None:
    #                 # Authenticate the student
    #                 authenticated_student = authenticate(request, email=email, password=password)
    #                 if authenticated_student is not None:
    #                     login(request, authenticated_student)
    #                     return redirect(reverse('documents'))
    #                 else:
    #                     messages.error(request, 'Invalid email or password.')
    #             else:
    #                 messages.error(request, 'Student does not exist.')
        
    #return render(request, 'login.html', {'form': form})
     form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            # Check if the student exists
            try:
               
                student = Student.objects.get(email=email)
            except Student.DoesNotExist:
                student = None

            if student is not None:
                # Authenticate the student
                authenticated_student = authenticate(request, email=email, password=password)
                if authenticated_student is not None:
                    login(request, authenticated_student)
                    return redirect('services')
                else:
                    messages.error(request, 'Invalid email or password.')

            else:
                # Check if the tutor exists
                try:
                    tutor = Tutor.objects.get(email=email)
                except Tutor.DoesNotExist:
                    tutor = None

                if tutor is not None:
                    # Authenticate the tutor
                    authenticated_tutor = authenticate(request, email=email, password=password)
                    if authenticated_tutor is not None:
                        login(request, authenticated_tutor)
                        return redirect('services')
                    else:
                        messages.error(request, 'Invalid email or password.')
                else:
                    messages.error(request, 'User does not exist.')

    return render(request, 'login.html', {'form': form})