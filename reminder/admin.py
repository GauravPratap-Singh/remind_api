from django.contrib import admin
from .models import Remind

# Register your models here.
class RemindAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'message')

# Register your models here.

admin.site.register(Remind, RemindAdmin)