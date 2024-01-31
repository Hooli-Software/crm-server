from django.contrib import admin

from . import models

@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'owner',
        'date_created',
    )


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'project',
        'date_created'
    )


@admin.register(models.Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        'datetime_start',
        'datetime_finish'
    )