from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'title']


admin.site.register(Order, OrderAdmin)