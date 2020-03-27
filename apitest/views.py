from django.shortcuts import render
from django.http import HttpResponse
from apitest.models import Apitest, Apistep
from django.contrib.auth.decorators import login_required

# Create your views here.


def test(request):
    return HttpResponse("Hello World")

# 接口管理
@login_required
def apitest_manage(request):
    apitest_list = Apitest.objects.all()
    username = request.session.get('user',"")
    return render(request,"apitest_manage.html",{"user":username,"apitests":apitest_list})

# 接口步骤管理
@login_required
def apistep_manage(request):
    username = request.session.get("user", "")
    apistep_list = Apistep.objects.all()
    return render(request, "apistep_manage.html", {"user" : username, "apisteps": apistep_list})

