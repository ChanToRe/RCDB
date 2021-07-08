from django.shortcuts import render
from django.http import HttpResponse
from .models import rcdb
from django.contrib.auth.models import User
from django.core import serializers
#def index(request):
#   return render(request, 'rcdb/index.html')

def get_RCDB(request):
    rcdbs = rcdb.objects.all()
    rcdb_list = serializers.serialize('json', rcdbs)
    return HttpResponse(rcdb_list, content_type="text/json-comment-filtered")

def apiRCDB(request):
    return render(request, 'rcdb/index.html')