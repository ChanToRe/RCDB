from django.contrib import admin
from .models import Notice

class NoticeAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Notice, NoticeAdmin)