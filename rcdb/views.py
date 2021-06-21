from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Notice

# Create your views here.
def index(request):
    notice_list = Notice.objects.order_by('-create_date')
    context = {'notice_list': notice_list}
    return render(request, 'rcdb/notice_list.html', context)

def detail(request, notice_id):
    notice = get_object_or_404(Notice, pk=notice_id)
    context = {'notice' : notice}
    return render(request, 'rcdb/notice_detail.html', context)