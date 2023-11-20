from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def virat(request):
    return render(request,'virat.html')
def maxi(request):
    return HttpResponse('<h1>he is the first batsman to score a double hundred in the lower order</h1>')

