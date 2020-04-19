from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from help_function.log_print import log_write


def login(request):
    if request.POST:
        username = password = ""
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            request.session["user"] = username

            response = HttpResponseRedirect("/home/")
            log_write('这是个debug消息')
            # response = HttpResponseRedirect("http://www.baidu.com")
            return response
        else:
            return render(request, 'login.html', {"error": "username or password error"})
    return render(request, "login.html")

def home(request):
    return render(request, "home.html")

def logout(request):
    auth.logout(request)
    return render(request, 'login.html')
