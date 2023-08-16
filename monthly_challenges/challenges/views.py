from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

month_challenge = {
    "january" : "This is January.....",
    "february" : "This is February",
    "march" : "This is March........",
    "april" : "This is April",
    "may" : "This is May......"
}

# Create your views here.

def index(request):
    list_items =""
    months = list(month_challenge.keys())
    for month in months:
        month_path = reverse("month-challenge", args=[month])
        list_items+= f"<li><a href=\"{month_path}\">"f"<h1>{month.capitalize()}</h1></a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenges(request,month):
    try:
        challenge_text = month_challenge[month]
        response_data = f"<h1>{challenge_text}<h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This Page is not Valid<h1>")

def monthly_challenges_by_number(request,month):
    month_name= list(month_challenge.keys())
    if(month > len(month_name)):
        return HttpResponseNotFound("Invalid Month")
    forwarded_month = month_name[month-1]
    redirect_path = reverse("month-challenge", args=[forwarded_month]) #/challenges/january
    return HttpResponseRedirect(redirect_path)