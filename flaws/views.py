from django.shortcuts import render
from django.http import HttpResponse
import sqlite3
from .models import Account
from django.contrib.auth.models import User


# Create your views here.


def index(request):
    return render(request, "pages/index.html", {"users": User.objects.all()})


##INJECTION
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
def informationView(request):
    user = User.objects.filter(username=request.GET.get("user")).first()

    accounts = Account.objects.filter(owner=user).all()
    return render(
        request,
        "pages/index.html",
        {"accounts": accounts, "user": user, "users": User.objects.all()},
    )


##LOGGING IN IS DONE IN A WAY THAT SESSION KEY IS TRIVIALLY RECOREVABLE AND CAN BE USED TO SNIFF OTHER USERS DATA
