from django.contrib import admin

from . import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'path'
    )


@admin.register(models.Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = (
        'start', 
        'end',
        'duration',
    )