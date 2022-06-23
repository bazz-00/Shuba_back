from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created')  # какие поля модели мы будем видеть в админке


admin.site.register(Order, OrderAdmin)
