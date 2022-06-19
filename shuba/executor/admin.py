from django.contrib import admin
from .models import Executor


class ExecutorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


admin.site.register(Executor, ExecutorAdmin)
