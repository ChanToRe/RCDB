from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'info/index.html')

def candidates(request, name):
    candidate = get_object_or_404(Candidate, name = name)
    return HttpResponse(candidate.name)