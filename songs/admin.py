from django.contrib import admin
from . import models

@admin.register(models.Song)
class SongAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Rank)
class RankAdmin(admin.ModelAdmin):
    pass

