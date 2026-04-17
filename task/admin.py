from django.contrib import admin
from .models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
  list_display = ("id","task", "status","workspace")
  
admin.site.register(Task, TaskAdmin)