# coding: utf-8
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.contrib import auth
from account import form as AccountForm
from account import models
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

#
def login_form(request):
    obj = AccountForm.LoginForm(request.POST)
    if request.method == "POST":
        if obj.is_valid():
            all_data = obj.clean()
        else:
            # Form表单的提交
            error = obj.errors
            print type(error)
            print error['username']
            # Ajax
            error = obj.errors.as_json()
            print type(error)
        return render(request, 'account/login.html', {'obj': obj})
    return render(request, 'account/login.html', {'obj': obj})


def logout(request):
    return render_to_response("login.html")


def base(request):
    return render_to_response("base.html")
    # before = models.UserInfo.objects.all()
    # # models.UserInfo.objects.create(username='aliex2',typeId_id=2)
    # after = models.UserInfo.objects.all()
    #
    # print before
    # print after


def assets(request):
    user_dict = request.session.get('username', None)
    if user_dict:
        return render_to_response("assets.html", {'username': user_dict})
    else:
        return redirect('/login/')


def user_manage(request):
    return render_to_response("user_manage.html")

