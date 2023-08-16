from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def index(request):
    return HttpResponse("This works!")
def index2(request):
    return HttpResponse("This works2!")
def index3(request):
    return HttpResponse("This works3!")
def index4(request):
    return HttpResponse("This works4!")

def monthly_challenges(request,month):
    challenge_text = None
    if(month == 'january'):
        challenge_text = "Prepare Yourself......"
    elif(month == 'february'):
        challenge_text = "Get Ready......"
    else:
        return HttpResponseNotFound("This is not a valid URL")
    return HttpResponse(challenge_text)