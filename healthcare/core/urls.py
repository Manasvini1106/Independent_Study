from django.urls import path, include
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.template.response import TemplateResponse

def index(request):
    return TemplateResponse(request, 'home.html', {})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.registerView, name='reg'),
    path('reg_user/', views.registerUser, name='reg_user'),
    path('login/', views.loginView, name='login'),
    path('patient/', views.patient_home, name='patient'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('diagnosis/', views.diagnosis, name='diagnosis'),
    path('diagnosis/predict', views.MakePredict, name='predict'),
    path('result/', views.patient_result, name='result'),
    path('result/ment', views.MakeMent, name='ment'),
    path('ment/', views.patient_ment, name='ment_list'),
    path('logout/', views.logoutView, name='logout'),
    path('doctor/', views.doctor_home, name='doctor'),
    path('commend/', views.doctor_commend, name='commend'),
    path('commend/predict', views.MakeMend, name='mend'),
    path('meet/', views.doctor_ment, name='meet_list'),
    path('meet/save/', views.SaveMent, name='savement'),
    path('doctors/', views.doctor_list, name='dr_list'),
    path('about/', views.about, name='about'),
    path('register/', views.register_view, name='register_view'),
    path('login/', views.login_view, name='login_view'),
    path('doctors/', views.doctors, name='doctors'),
]