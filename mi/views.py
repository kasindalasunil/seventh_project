from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def rohit(request):
    return render(request,'rohit.html')
def sky(request):
    return HttpResponse('<h1>he is the new mr.360 to our indian team</h1>')
