from django.db import models

class Weather(models.Model):
    city = models.CharField(max_length=100)
    date = models.DateField()
    temperature = models.FloatField()
    pressure = models.FloatField()
    humidity = models.FloatField()
    precipitation = models.FloatField()
    weather_condition = models.CharField(max_length=100)

    def __str__(self):
        return (
            f"ID: {str(self.id)}, City: {self.city}, Date: {self.date}, "
            f"Temperature: {self.temperature}, Pressure: {self.pressure}, "
            f"Humidity: {self.humidity}, Precipitation: {self.precipitation}, "
            f"Condition: {self.weather_condition}"
        )
