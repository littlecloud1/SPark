from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    # this use index.html to perform HttpResponse
    return render(request,'index.html')
