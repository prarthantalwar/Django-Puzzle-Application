from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core import serializers
from app1.models import Player


# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("Password and confirm password doesn't match")
        else:
            player=Player(username=uname, email=email, score=0)
            player.save()
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    

    return render (request,'index.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect ('home')
        else:
            return HttpResponse("Username and passowrd doesn't match")
    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')


def Clue1Page(request):
    if request.method=='POST':
        ans=request.POST.get('answer')
        if ans.upper() =="ASIA":
            name=request.user.username
            player_list=Player.objects.all()
            scor=GetScore(name, player_list)
            scor=scor+10
            Player.objects.filter(username=name).update(score=scor)
            # Print that the user got correct answer for clue 1 using alert, increase the user score
            return redirect ('clue2')
        else:
            name=request.user.username
            player_list=Player.objects.all()
            scor=GetScore(name, player_list)
            scor=scor-2
            Player.objects.filter(username=name).update(score=scor)
            messages.warning(request, "Your answer is wrong. Try again. 2 points deducted.")
             # Give alert that answer is wrong, and they have to try again
                # Reduce score
    return render (request,'clue1.html')

def Clue2Page(request):
    if request.method=='POST':
        ans=request.POST.get('answer')
        if ans.upper() =="QUEST":
            name=request.user.username
            player_list=Player.objects.all()
            scor=GetScore(name, player_list)
            scor=scor+10
            Player.objects.filter(username=name).update(score=scor)
            # Print that the user got correct answer for clue 1 using alert, increase the user score
            return redirect ('clue3')
        else:
            name=request.user.username
            player_list=Player.objects.all()
            scor=GetScore(name, player_list)
            scor=scor-2
            Player.objects.filter(username=name).update(score=scor)
            messages.warning(request, "Your answer is wrong. Try again. 2 points deducted.")
            # Give alert that answer is wrong, and they have to try again
                # Reduce score
    return render (request,'clue2.html')

def Clue3Page(request):
    if request.method=='POST':
        ans=request.POST.get('answer')
        if int(ans) ==12:
            name=request.user.username
            player_list=Player.objects.all()
            scor=GetScore(name, player_list)
            scor=scor+10
            Player.objects.filter(username=name).update(score=scor)
            # Print that the user got correct answer for clue 1 using alert, increase the user score
            return redirect ('clue4')
        elif int(ans)==78 or int(ans)==20 :
            return redirect('dead1')
        else:
            name=request.user.username
            player_list=Player.objects.all()
            scor=GetScore(name, player_list)
            scor=scor-2
            Player.objects.filter(username=name).update(score=scor)
            messages.warning(request, "Your answer is wrong. Try again. 2 points deducted.")
            # Give alert that answer is wrong, and they have to try again
                # Reduce score
    return render (request,'clue3.html')

def Clue4Page(request):
    if request.method=='POST':
        ans=request.POST.get('answer')
        if ans.upper() =="SEVEN":
            name=request.user.username
            player_list=Player.objects.all()
            scor=GetScore(name, player_list)
            scor=scor+10
            Player.objects.filter(username=name).update(score=scor)
            # Print that the user got correct answer for clue 1 using alert, increase the user score
            return redirect ('clue5')
        elif ans.upper()=="NINE":
            return redirect('dead2')
        else:
            name=request.user.username
            player_list=Player.objects.all()
            scor=GetScore(name, player_list)
            scor=scor-2
            Player.objects.filter(username=name).update(score=scor)
            messages.warning(request, "Your answer is wrong. Try again. 2 points deducted.")
            # Give alert that answer is wrong, and they have to try again
                # Reduce score
    return render (request,'clue4.html')

def Clue5Page(request):
    if request.method=='POST':
        ans=request.POST.get('answer')
        if ans.upper() =="TREASURE":
            name=request.user.username
            player_list=Player.objects.all()
            scor=GetScore(name, player_list)
            scor=scor+10
            Player.objects.filter(username=name).update(score=scor)
            # Print that the user got correct answer for clue 1 using alert, increase the user score
            return redirect ('winner')
        else:
            name=request.user.username
            player_list=Player.objects.all()
            scor=GetScore(name, player_list)
            scor=scor-2
            Player.objects.filter(username=name).update(score=scor)
            messages.warning(request, "Your answer is wrong. Try again. 2 points deducted.") 
            # Give alert that answer is wrong, and they have to try again
                # Reduce score
    return render (request,'clue5.html')

def Dead1Page(request):
    name=request.user.username
    player_list=Player.objects.all()
    scor=GetScore(name, player_list)
    scor=scor-5
    Player.objects.filter(username=name).update(score=scor)
    messages.warning(request, "You have reached a dead end. 5 points deducted.")
    # Tell they've reached a deadend, reduce score, give link to go back to previous clue
    return render (request,'dead1.html')

def Dead2Page(request):
    name=request.user.username
    player_list=Player.objects.all()
    scor=GetScore(name, player_list)
    scor=scor-5
    Player.objects.filter(username=name).update(score=scor)
    messages.warning(request, "You have reached a dead end. 5 points deducted.")
    # Tell they've reached a deadend, reduce score, give link to go back to previous clue
    return render (request,'dead2.html')

def WinnerPage(request):
    name=request.user.username
    player_list=Player.objects.all()
    score=GetScore(name, player_list)
    context={"Score": score}
    return render (request,'winner.html',context)


def GetScore(name, player_list):
    for player in player_list:
        if player.username == name:
            score = player.score
            break
    return score

# Fetching analytics and tables
def analytics(request):
    data = serializers.serialize("python",Player.objects.order_by('score'))
    
    return render(request,'table.html',{'data':data})



