from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Notice
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    notice_list = Notice.objects.order_by('-create_date')
    context = {'notice_list': notice_list}
    return render(request, 'notice/notice_list.html', context)

def detail(request, notice_id):
    notice = get_object_or_404(Notice, pk=notice_id)
    context = {'notice' : notice}
    return render(request, 'notice/notice_detail.html', context)

def index(request):
    page = request.GET.get('page', '1')
    notice_list = Notice.objects.order_by('-create_date')
    paginator = Paginator(notice_list, 15)
    page_obj = paginator.get_page(page)
    context = {'notice_list': page_obj}
    return render(request, 'notice/notice_list.html', context)