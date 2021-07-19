from django.contrib import admin
from .models import rcdb

class RcdbAdmin(admin.ModelAdmin):
    search_fields = ['LabID']

admin.site.register(rcdb, RcdbAdmin)