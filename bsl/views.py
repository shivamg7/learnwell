
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
import random



from .models import Question,user,Attempt,Stats
import matplotlib.pyplot as plt
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
        return HttpResponseRedirect(reverse('bsl:dashboard'))
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
    userVar = user.objects.get(id=request.user.id)
    scoreVar = Stats.objects.filter(userV=userVar)

    return render(request,'bsl/dashboard.html',{'scores':scoreVar})


def showQuiz(request):
    #Get some question from the database
    count = Question.objects.all().count()
    userVar = user.objects.get(id=request.user.id)
    rating = userVar.rating

    if(userVar.lower_bound==0):
        lower_bound = rating-50
        upper_bound = rating+150
        userVar.lower_bound = lower_bound
        userVar.upper_bound = upper_bound

    userVar.score = 0
    range_ = userVar.upper_bound - userVar.lower_bound
    range_ = range_/3
    lower_bound = userVar.lower_bound
    threshold = userVar.lower_bound + range_

    myQuestions = Question.objects.filter(rating__gt=lower_bound,rating__lt=threshold)
    print(str(lower_bound)+" : "+str(threshold))
    count = len(myQuestions)
    slice = (int(random.random()*(1000)))%count
    myQuestion = Question.objects.all()[slice: slice+1]
    userVar.save()
    #render pages
    return render(request, 'bsl/quiz.html', {'question':myQuestion[0]})

def submitAnswer(request,questionId,answer):
    print(request.POST['clicks'])
    print(request.POST['time_diff'])
    clicks = request.POST['clicks']
    time_diff = int(float(request.POST['time_diff']))
    td = int(time_diff)
    answer = request.POST.get('ans')
    questionVar = Question.objects.get(id=questionId)

    userVar = user.objects.get(id=request.user.id)
    c_level_avg = userVar.c_level_avg
    c_level = 0
    q_ratingChange = questionVar.ratingChange
    userVar.question_count = userVar.question_count+1
    questionVar.counter += 1
    userVar.save()
    questionVar.save()
    n = questionVar.counter
    i = userVar.question_count
    if(questionVar.answer==answer):
        result = 'C'
    else:
        result = 'W'

    if(result=='C'):
        userVar.score += 1
        nc = request.POST['clicks']
        nc = int(nc)
        l= userVar.lower_bound
        u = userVar.upper_bound


        q_rating = questionVar.rating
        q_ratingChange = questionVar.ratingChange

        bt = 0
        if q_rating <= l+66:
            bt = 5
        elif q_rating <= l+132:
            bt = 10
        else:
            bt = 20

        print(str(type(bt))+" : "+str(type(td)))
        print(td)
        if td <= bt:
            c1 = 1
        elif td>bt and td<2*bt:
            c1 = .6
        else:
            c1 = .3

        if nc == 1:
            c2 = 1
        elif nc == 2:
            c2 = .7
        elif nc == 3:
            c2 = .5
        else:
            c2 = .25

        c_level = ((2*c2)+c1)*100/3
        print("C LEVEL"+str(c_level))
        print("c1 and c2"+str(c1)+str(c2))

    else:
        c_level = -100

    userVar.cSum += c_level
    print("C LEVEL"+str(c_level))
    c_level_avg = ((c_level_avg*(i-1))+c_level)/i
    if(i%3==0):
        if(userVar.cSum<-40):
            if(userVar.lower_bound>70):
                userVar.lower_bound-=66
                userVar.upper_bound-=66
        elif(userVar.cSum>130):
            if(userVar.upper_bound<940):
                userVar.lower_bound+=66
                userVar.lower_bound+=66
        userVar.cSum = 0



    q_ratingChange = ((q_ratingChange*(n-1))+c_level)/n
    questionVar.q_ratingChange = q_ratingChange

    if n==5:
        if q_ratingChange<0:
            neg = -1
        else:
            neg = 1
        if q_ratingChange<=20:
            questionVar.rating = questionVar.rating+(neg*10)
        elif q_ratingChange<=40 and q_ratingChange>20:
            questionVar.rating = questionVar.rating+(neg*20)
        elif q_ratingChange<=60 and q_ratingChange>40:
            questionVar.rating = questionVar.rating+(neg*30)
        elif q_ratingChange<=80 and q_ratingChange>60:
            questionVar.rating = questionVar.rating+(neg*40)
        elif q_ratingChange>80:
            questionVar.rating = questionVar.rating+(neg*50)

        questionVar.q_ratingChange = 0
        questionVar.counter = 0
    print("Ic ounter" + str(i))
    if i==10:
        userVar.question_count = 0
        if c_level_avg<0:
          neg = -1
        else:
          neg = 1
        if c_level_avg<=20:
          userVar.rating = userVar.rating+(neg*20)
        elif c_level_avg<=40 and c_level_avg>20:
          userVar.rating = userVar.rating+(neg*40)
        elif c_level_avg<=60 and c_level_avg>40:
          userVar.rating = userVar.rating+(neg*60)
        elif c_level_avg<=80 and c_level_avg>60:
          userVar.rating = userVar.rating+(neg*80)
        elif c_level_avg>80:
          userVar.rating = userVar.rating+(neg*100)


        questionVar.save()
        userVar.save()
        print(answer+" correct is "+questionVar.answer)
        attempVar = Attempt(question=questionVar,userAtt=userVar,result=result,clicks=clicks,time_diff=time_diff)
        attempVar.save()
        myStat = Stats(userV=userVar,quizV=questionVar,score=userVar.score)

        return render(request,"bsl/results.html",{'userVar':userVar,'scores':scoreVar})

    questionVar.save()
    userVar.save()
    print(answer+" correct is "+questionVar.answer)
    attempVar = Attempt(question=questionVar,userAtt=userVar,result=result,clicks=clicks,time_diff=time_diff)
    attempVar.save()

    if(result=='C'):
        correctAnswer = "T"
        confi = c_level
    else:
        correctAnswer = "F"
        confi="None"

    print("Rendering feedback")
    print(questionVar.answer)
    if(answer=='A'):
        return render(request,'bsl/feedback.html',{'question':questionVar,'correctAnswer':correctAnswer,'optionA':"Checked",'confi':confi})
    if(answer=='B'):
        return render(request,'bsl/feedback.html',{'question':questionVar,'correctAnswer':correctAnswer,'optionB':"Checked",'confi':confi})
    if(answer=='C'):
        return render(request,'bsl/feedback.html',{'question':questionVar,'correctAnswer':correctAnswer,'optionC':"Checked",'confi':confi})
    if(answer=='D'):
        return render(request,'bsl/feedback.html',{'question':questionVar,'correctAnswer':correctAnswer,'optionD':"Checked",'confi':confi})



def results(request):
    return render(request,'bsl/results.html')


def stats(request):
    return
