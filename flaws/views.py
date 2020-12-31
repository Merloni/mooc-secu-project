from django.shortcuts import render, redirect

from django.http import HttpResponse
import sqlite3
from .models import Account, Message
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, "pages/index.html", {"users": User.objects.all()})


##INJECTION
@login_required
def injectionView(request):
    u = User.objects.filter(username="Tuomo").first()
    accounts = Account.objects.all()
    query = request.POST.get("query")
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    sqlquery = "SELECT id FROM auth_user WHERE username='%s'" % query
    response = cursor.execute(sqlquery).fetchall()
    users = User.objects.all()

    return render(
        request,
        "pages/index.html",
        {"queryresult": response, "query": query, "users": users},
    )


##SENSITIVE DATA EXPOSURE
@login_required
def informationView(request):
    user = User.objects.filter(username=request.GET.get("user")).first()

    accounts = Account.objects.filter(owner=user).all()
    return render(
        request,
        "pages/index.html",
        {"accounts": accounts, "user": user, "users": User.objects.all()},
    )


##LOGGING IN IS DONE IN A WAY THAT SESSION KEY IS TRIVIALLY RECOREVABLE AND CAN BE USED TO SNIFF OTHER USERS DATA


##HTML HAS |SAFE ON SO GIVEN MESSAGES ARE RAN AS ACTUAL HTML/JS
@login_required
def xssView(request):
    message = Message.objects.create(text=request.POST.get("message"))
    messages = Message.objects.all()
    return render(
        request,
        "pages/index.html",
        {"users": User.objects.all(), "messages": messages},
    )


@login_required
def deleteXssView(request):
    Message.objects.all().delete()
    return redirect("/")
