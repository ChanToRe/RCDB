from django.shortcuts import render
from django.http import HttpResponse
from .models import rcdb
from django.contrib.auth.models import User
from django.core import serializers
import json

def index(request):
    rcdbsDict = []

    for data in rcdb.objects.all():
        tmpdict = {
            "id" : data.id,
            "Name" : data.Name,
            "State" : data.State,
            "City": data.City,
            "Site" : data.Site,
            "Material" : data.Material,
            "Weight_g" : data.Weight_g,
            "Laboratory" : data.Laboratory,
            "LabID" : data.LabID,
            "Age_BP" : data.Age_BP,
            "Error" : data.Error,
            "Report" : data.Report
        }
        rcdbsDict.append(tmpdict)

    rcdbsJson = json.dumps(rcdbsDict, ensure_ascii=False)
    context = {'rcdbsJson' : rcdbsJson}
    return render(request, 'rcdb/index.html', context)
