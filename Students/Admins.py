from django.contrib import admin
from .models import Admins 

admin.site.register(Admins)

class Admins (admin.ModelAdmin):
    pass

admin.site.register(Admins )