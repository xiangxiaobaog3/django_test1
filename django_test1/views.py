# coding: utf-8
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.http import JsonResponse
# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            request.session['username'] = username
            return redirect('/assets/')
        else:
            return render_to_response('login.html')
    else:
        return render_to_response('login.html')


def logout(request):
    return render_to_response("login.html")


def base(request):
    return render_to_response("base.html")

def assets(request):
    user_dict = request.session.get('username', None)
    if user_dict:
        return render_to_response("assets.html", {'username': user_dict})
    else:
        return redirect('/login/')


def user_manage(request):
    return render_to_response("user_manage.html")

