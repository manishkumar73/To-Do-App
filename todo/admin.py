from django.contrib import admin

# Register your models here.
from .models import ToDoApp

admin.site.register(ToDoApp)
