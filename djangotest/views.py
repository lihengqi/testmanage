from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def djangotest(request):
    return HttpResponse("This is a django test")
