from django.contrib import admin
from .models import Executor, Speciality


class ExecutorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


class SpecialityAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Executor, ExecutorAdmin)
admin.site.register(Speciality, SpecialityAdmin)