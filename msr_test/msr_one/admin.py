from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(project_model)
class TaskBoardAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'created_by', 'created_on')
