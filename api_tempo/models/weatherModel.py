from django.db import models

class Weather(models.Model):
    city = models.CharField(max_length=100)
    date = models.DateTimeField()
    temperature = models.FloatField()
    pressure = models.FloatField()
    humidity = models.FloatField()
    precipitation = models.FloatField()
    weather_condition = models.CharField(max_length=100)
