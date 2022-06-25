from django.contrib import admin
from .models import Order, OrderComments


class OrderAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created')  # какие поля модели мы будем видеть в админке


class OrderCommentsAdmin(admin.ModelAdmin):
    list_display = ('order', 'user', 'body', 'created', 'is_active')
    list_filter = ('is_active', 'created', 'updated')
    search_fields = ('order', 'user', 'body')


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderComments, OrderCommentsAdmin)







