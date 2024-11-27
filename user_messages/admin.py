from django.contrib import admin
from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date','content', 'timestamp')
    search_fields = ('name', 'email', 'phone', 'date', 'content')
    list_filter = ('timestamp',)
