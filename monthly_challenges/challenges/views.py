from django.shortcuts import render
from django.http import Http404,HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

month_challenge = {
    "january" : "This is January.....",
    "february" : "This is February",
    "march" : "This is March........",
    "april" : "This is April",
    "may" : "This is May......",
    "december" : None
}

# Create your views here.

def index(request):
    months = list(month_challenge.keys())
    return render(request,"challenges/index.html",{
        "month_list" : months
    })

def monthly_challenges(request,month):
    try:
        challenge_text = month_challenge[month]
        return render(request, "challenges/challenge.html" , {
            "text" : challenge_text,
            "month" : month
        })
    except:
        return Http404

def monthly_challenges_by_number(request,month):
    month_name= list(month_challenge.keys())
    if(month > len(month_name)):
        return HttpResponseNotFound("Invalid Month")
    forwarded_month = month_name[month-1]
    redirect_path = reverse("month-challenge", args=[forwarded_month]) #/challenges/january
    return HttpResponseRedirect(redirect_path)