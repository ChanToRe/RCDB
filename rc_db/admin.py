from django.contrib import admin
from .models import rc_db

class Rc_DbAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(rc_db, Rc_DbAdmin)