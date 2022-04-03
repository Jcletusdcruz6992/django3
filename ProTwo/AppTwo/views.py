from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    help_dict={'help_me':"Help is on the way from views.py"}
    return render(request,'AppTwo\help.html',context=help_dict)
