"""
URL configuration for puzzleme project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views


admin.site.site_header = "PuzzleMe Admin"
admin.site.site_title = "PuzzleMe Admin Portal"
admin.site.index_title = "Welcome to PuzzleMe "

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('home/', views.HomePage, name='home'),
    path('logout/', views.LogoutPage, name='logout'),
    path('c1/', views.Clue1Page, name='clue1'),
    path('clu2/', views.Clue2Page, name='clue2'),
    path('cl3/', views.Clue3Page, name='clue3'),
    path('cluu4/', views.Clue4Page, name='clue4'),
    path('cl5/', views.Clue5Page, name='clue5'),
    path('dd11/', views.Dead1Page, name='dead1'),
    path('dud2/', views.Dead2Page, name='dead2'),
    path('win_ner/', views.WinnerPage, name='winner'),
    path('table/', views.analytics, name='analytics')

]
