from django.http import response
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
from .models import *
from django.contrib import messages

# Create your views here.

def index(request):
    request.session['id']=0
    return render(request, 'index.html')
def login(request):
    request.session['id']=0
    return render(request, 'login.html')
def register(request):
    request.session['id']=0
    return render(request, 'register.html')
def create(request):
    errors = User.objects.registration_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/register')
    x=request.POST
    newUser=User.objects.create(first_name=x['fname'], last_name=x['lname'], email= x['email'],  password= x['pw'])
    request.session['id']=newUser.id
    return redirect('/homepage')
def validate(request):
    x=request.POST
    errors = User.objects.login_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/login')
    user= User.objects.filter(email=x['email'])
    request.session['id']=user[0].id
    return redirect('/homepage')
def homepage(request):
    if request.session['id']==0:
        return redirect('/login')
    x= request.session['id']
    allQuotes= Quote.objects.all()
    allusers=User.objects.all()
    context ={
        'loggedin': User.objects.get(id=x),
        'quotes': allQuotes,
        'users':allusers
    }
    return render(request, 'homepage.html', context)
def logout(request):
    request.session['id']=0
    return redirect('/login')
def editAccount(request):
    if request.session['id']==0:
        return redirect('/login')
    x= request.session['id']
    context ={
        'loggedin': User.objects.get(id=x)
    }
    return render(request, 'editAccount.html', context)
def update(request):
    x= request.session['id']
    user= User.objects.get(id=x)
    y=request.POST
    errors = User.objects.update_validator(request.POST,user)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/edit/account')
    user.first_name=y['fname']
    user.last_name=y['lname']
    user.email=y['email']
    user.save()
    return redirect('/homepage')
def createQuote(request):
    x= request.session['id']
    loggedinuser=User.objects.get(id =x)
    y=request.POST
    errors= User.objects.quote_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/homepage')
    Quote.objects.create(author=y['author'], quote=y['quote'], user=loggedinuser)
    return redirect('/homepage')
def viewQuotes(request, x):
    y= User.objects.get(id=x)
    z=request.session['id']
    context={
        'user': y,
        'quotes': Quote.objects.all(),
        'loggedin': User.objects.get(id=z)
        
    }
    return render(request, 'userQuotes.html', context)
def deleteQuote(request,x):
    quoteToDelete= Quote.objects.get(id=x)
    quoteToDelete.delete()
    return redirect('/homepage')
def likeQuote(request,x):
    y= request.session['id']
    currentuser= User.objects.get(id=y)
    quoteToLike= Quote.objects.get(id=x)
    currentuser.liked_quotes.add(quoteToLike)
    return redirect('/homepage')
    