from django.contrib import admin
from .models import rcdb

class RcdbAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(rcdb, RcdbAdmin)