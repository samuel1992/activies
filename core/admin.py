from django.contrib import admin
from core.models import Task

class TaskAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        (None, {'fields': ['description']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Task, TaskAdmin,)