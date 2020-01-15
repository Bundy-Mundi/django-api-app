from django.db import models
from core.models import CoreModel
from songs.models import Song

class YearlyChart(CoreModel):
    
    year_choices = [
        (2020, "2020"),
        (2021, "2021"),
        (2022, "2022"),
        (2023, "2023"),
        (2024, "2024"),
        (2025, "2025"),

    ]

    year = models.IntegerField(choices=year_choices)
    songs = models.ManyToManyField("songs.Song")

    class Meta:
        verbose_name_plural = "Yearly Charts"

    def __str__(self):
        return str(self.year)

class MonthlyChart(CoreModel):

    JANUARY	= "JAN"
    FEBRUARY = "FEB"
    MARCH = "MAR"
    APRIL	= "APR"
    MAY	= "MAY"
    JUNE = "JUN"
    JULY = "JUL"
    AUGUST = "AUG"
    SEPTEMBER = "SEP"
    OCTOBER = "OCT"
    NOVEMBER = "NOV"
    DECEMBER = "DEC"

    month_choices = [

        ( JANUARY, "January" ),
        ( FEBRUARY, "Feburary" ),
        ( MARCH, "March" ),
        ( APRIL, "April" ),
        ( MAY, "May" ),
        ( JUNE, "June" ),
        ( JULY, "July" ),
        ( AUGUST, "August" ),
        ( SEPTEMBER, "September" ),
        ( OCTOBER, "October" ),
        ( NOVEMBER, "November" ),
        ( DECEMBER, "December" ),

    ]

    month = models.CharField(choices= month_choices, max_length=3)
    songs = models.ManyToManyField("songs.Song")

    class Meta:
        verbose_name_plural = "Monthly Charts"

    def __str__(self):
        return str(self.month)

class WeeklyChart(CoreModel):
    # week_choices = 
    # week = models.IntegerField(choices=)
    songs = models.ManyToManyField("songs.Song")

    class Meta:
        verbose_name_plural = "Weekly Charts"

    def __str__(self):
        return str(self.week)

class Chart(models.Model):

    BILLBOARD_HOT_100 = "BB_100"
    BILLBOARD_HOT_200 = "BB_100"

    chart_name_choices = [
        (BILLBOARD_HOT_100, "Billborad Hot 100"),
        (BILLBOARD_HOT_200, "Billborad Hot 200"),
    ]

    name = models.CharField(choices=chart_name_choices, max_length=10)
    year = models.ForeignKey("YearlyChart", on_delete=models.CASCADE, default="")
    month = models.ForeignKey("MonthlyChart", on_delete=models.CASCADE,  default="")
    week = models.ForeignKey("WeeklyChart", on_delete=models.CASCADE,  default="")
    
    def __str__(self):
        return self.name
