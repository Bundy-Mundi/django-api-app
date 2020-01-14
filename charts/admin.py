from django.contrib import admin
from . import models

@admin.register(models.ChartNames)
class ChartAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Years)
class ChartAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Months)
class ChartAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Weeks)
class ChartAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Chart)
class ChartAdmin(admin.ModelAdmin):
    list_display = ("__str__",)
