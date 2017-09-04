from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.http import JsonResponse
# Create your views here.

class login(request):
    if request.method == "POST":

        username = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        ret = {"status": 0, "errmsg": ""}
        if user:
            return HttpResponseRedirect('/assets/')
        else:
            ret["status"] = 1
            ret["errmsg"] = "用户名和密码错误，请联系管理员."
            return JsonResponse(ret)
    else:
        return HttpResponseRedirect('/assets/')

