from django.db import models
from core.models import CoreModel
from songs.models import Song

class ChartNames(CoreModel):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Chart Names"
    
    def __str__(self):
        return self.name

class Years(CoreModel):
    year = models.IntegerField()

    class Meta:
        verbose_name_plural = "Years"

    def __str__(self):
        return str(self.year)

class Months(CoreModel):
    month = models.IntegerField()
    month_name = models.CharField(max_length=2)

    class Meta:
        verbose_name_plural = "Months"

    def __str__(self):
        return str(self.month)

class Weeks(CoreModel):
    week = models.IntegerField()

    class Meta:
        verbose_name_plural = "Weeks"

    def __str__(self):
        return str(self.week)

class Chart(models.Model):
    name = models.ForeignKey("ChartNames", on_delete=models.CASCADE, default="")
    year = models.ForeignKey("Years", on_delete=models.CASCADE, default="")
    month = models.ForeignKey("Months", on_delete=models.CASCADE,  default="")
    week = models.ForeignKey("Weeks", on_delete=models.CASCADE,  default="")
    
    def __str__(self):
        return self.name
