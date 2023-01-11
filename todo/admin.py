from django.contrib import admin

from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'created_by', 'assigned_to', 'completed',)
    exclude = ('created_by',)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user

        super().save_model(request, obj, form, change)
