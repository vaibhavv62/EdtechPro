from django.contrib import admin
from .models import Lead

# Register your models here.
class LeadModelAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Lead._meta.fields]
    # list_display = ['date','handled_by','']

admin.site.register(Lead,LeadModelAdmin)