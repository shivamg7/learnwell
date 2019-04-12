
from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
import smtplib


# Create your views here.

def index(request):
    
    if request.user.is_authenticated:
        userId = User.objects.get(id=request.user.id)
        return HttpResponseRedirect(reverse('bsl:dashboard'))
    else:
        return render(request, 'bsl/index.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('bsl:index'))

def login_(request):

    print("Login Request")
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('bsl:dashboard'))

    try:
        log_in = request.POST['login']
    except MultiValueDictKeyError:
        return render(request, 'bsl/login.html')

    print("Login Post request")
    try:
        username = request.POST['username']
        password = request.POST['password']
    except MultiValueDictKeyError:
        error_message = "Missing Credentials"
        return HttpResponseRedirect(reverse('bsl:dashboard'))

    print("User getting auth")
    user = authenticate(request, username=username,password=password)
    if user is not None:
        login(request, user)
        print("login Successful")
        print (user.username)
        return render(request,'bsl/index.html',{'user':user})
    else:
        error_message = "Wrong Credentials"
        print("Login Failed")
        return render(request, 'bsl/login.html', {'error_message':error_message})

def register(request):

    errors = []
    #Check if the registeration button has been clicked
    try:
        new_registration = request.POST['register']
    except MultiValueDictKeyError:
        return render(request, 'bsl/register.html')

    try:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password_1']
        confirm_password = request.POST['password_2']
    except MultiValueDictKeyError:
        errors.append("Missing elements in form.")

    if len(errors)==0:
        if password!=confirm_password:
            errors.append("Passwords do not match.")
            registered = 'False'
        else:
            registered = register_user(username,email,password)
            #try to register user



    if len(errors)==0 and registered=='success':
            user = authenticate(request, username=username,password=password)
            login(request, user)
            return HttpResponseRedirect(reverse('bsl:fillProfile'))
    else:
        errors.append(registered)
        return render(request, 'bsl/register.html', {'error_message':errors})

def register_user(usr,mail,passcode):

    print("Trying to register user")
    try:
        test_username = User.objects.get(username=usr)
    except User.DoesNotExist:
        user = User.objects.create_user(usr, mail, passcode)
        user.save()
        return "success"

    return "Username is already registered"


def dashboard(request):
    return render(request,'bsl/dashboard.html')
