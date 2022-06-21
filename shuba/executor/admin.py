from django.contrib import admin
from .models import Executor, Speciality, Orders


class ExecutorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


class SpecialityAdmin(admin.ModelAdmin):
    list_display = ['title']


class OrdersAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Executor, ExecutorAdmin)
admin.site.register(Speciality, SpecialityAdmin)
admin.site.register(Orders, OrdersAdmin)