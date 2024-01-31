from django.contrib import admin

from . import models


@admin.register(models.HabitCategory)
class HabitCategoryAdmin(admin.ModelAdmin):
    search_fields = (
        'parent',
    )
    autocomplete_fields = (
        'parent',
    )
    list_display = (
        '__str__',
        'parent',
        'created',
    )


@admin.register(models.HabitUnit)
class HabitUnitAdmin(admin.ModelAdmin):
    autocomplete_fields = (
        'category',
    )
    list_display = (
        'value',
        'datetime',
        'category'
    )


@admin.register(models.PeriodCategory)
class PeriodCategoryAdmin(admin.ModelAdmin):
    search_fields = (
        'parent',
    )
    autocomplete_fields = (
        'parent',
    )
    list_display = (
        '__str__',
        'parent',
        'created'
    )


@admin.register(models.PeriodUnit)
class PeriodUnitAdmin(admin.ModelAdmin):
    list_display = (
        'datetime_start',
        'datetime_end',
        'category'
    )


@admin.register(models.PeriodMessage)
class PeriodMessageAdmin(admin.ModelAdmin):
    list_display = (
        'datetime',
        'unit'
    )