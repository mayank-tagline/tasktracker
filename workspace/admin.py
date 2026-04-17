from django.contrib import admin
from .models import WorkSpace

class WorkSpaceAdmin(admin.ModelAdmin):
  list_display = ("id","name",)
  
admin.site.register(WorkSpace, WorkSpaceAdmin)