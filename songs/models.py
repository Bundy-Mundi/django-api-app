from django.db import models
from core.models import CoreModel


class Rank(CoreModel):
    song = models.ForeignKey("Song", related_name="which_song", on_delete=models.CASCADE)
    chart = models.ForeignKey("charts.Chart", related_name="which_chart", on_delete=models.CASCADE)
    rank = models.IntegerField()

class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    #album_image_url = 
    #artist_image_url = 
    charts = models.ManyToManyField("charts.Chart", related_name="charts")
    rank = models.ManyToManyField("Rank", related_name="ranks")