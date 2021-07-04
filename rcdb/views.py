from django.shortcuts import render
from django.http import HttpResponse
from .models import rcdb
from django.contrib.auth.models import User

#Create your views here.
def index(request):
    return render(request, 'rcdb/index.html')