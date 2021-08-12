from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def home(request):
    #return HttpResponse('Hello there') 
    return render(request, 'generator/home.html',{'password':'kfjkabvkjsdck'})

def password(request):

    letter = list('qazwsxedcrftgbyhnujmikolp')

    length = int(request.GET.get('length',8))
    if request.GET.get('UpperCase'):
        letter += list('qazwsxedcrftgbyhnujmikolp'.upper())
    
    if request.GET.get('Numbers'):
        letter += list('1234567890')

    if request.GET.get('SpecialChar'):
        letter += list('!@#$%^&*()_+}{?|')

    password =''.join([j for j in [random.choice(letter) for i in range(length)]])
    return render(request,'generator/password.html',{'password':password})

def about(request):
    return render(request,'generator/about.html')