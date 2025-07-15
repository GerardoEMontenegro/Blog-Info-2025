from django.contrib import admin
from .models import post

class postAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'ultima_actualizacion')

admin.site.register(post, postAdmin)