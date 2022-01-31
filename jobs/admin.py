from django.contrib import admin
from .models import Job

# Register your models here.


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    pass
