from django.shortcuts import render
from django.http import HttpResponse
from .models import rc_db

# Create your views here.
def index(request):
    return render(request, 'rc_db/index.html')