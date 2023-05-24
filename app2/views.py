from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app2_views(requesrt):
    return HttpResponse('<marquee>this is app2 views funtion of string response</marquee>')
def app2_html(request):
    return render(request,'app2_html.html')