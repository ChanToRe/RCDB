from django.contrib import admin
from .models import rcdb

class RcdbAdmin(admin.ModelAdmin):
    search_fields = ['Name']

admin.site.register(rcdb, RcdbAdmin)