from django.contrib import admin
from . import models

@admin.register(models.YearlyChart)
class ChartAdmin(admin.ModelAdmin):
    pass

@admin.register(models.MonthlyChart)
class ChartAdmin(admin.ModelAdmin):
    pass

@admin.register(models.WeeklyChart)
class ChartAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Chart)
class ChartAdmin(admin.ModelAdmin):
    list_display = ("__str__",)
