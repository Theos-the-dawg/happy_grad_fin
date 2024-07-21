from django.urls import path, include
from .views import (home,login_view,logout_view,services,create_Student,
                     create_Tutor,useful_links,documents,join_the_team)

urlpatterns = [
     path('home/',home,name='home'),#home
     path('login/',login_view,name='login'),#login
     path('logout/', logout_view, name='logout'),#logout
     path('services/',services,name='services'),#services page
     path('useful_links/', useful_links,name='useful_links'),#links and contacts
     path('signup_student/', create_Student, name='create_student'),#creation of student profile
     path('signup_tutor/',create_Tutor,name='create_tutor'),#creation of tutor profile
     path('documents/',documents,name='documents'),#logic for requesting a service via document
     path('join_the_team/',join_the_team,name='join_the_team'),# contact us page
]