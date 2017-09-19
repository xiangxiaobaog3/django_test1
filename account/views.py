from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.http import JsonResponse
from account import form as AccountForm
# Create your views here.

class login(request):
    obj = AccountForm.ALogin(request.POST)
    if request.method == "POST":



