from django.contrib import admin

from . import models

class SnoteAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(models.Snote, SnoteAdmin)