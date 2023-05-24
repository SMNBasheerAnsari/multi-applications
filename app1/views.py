from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app1_views(requesrt):
    return HttpResponse('<marquee>this is app1 views funtion of string response</marquee>')
def app1_html(request):
    return render(request,'app1_html.html')