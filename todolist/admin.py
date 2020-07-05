from django.contrib import admin
from .models import ToDo

class ToDoAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'due_date')

admin.site.register(ToDo, ToDoAdmin)

