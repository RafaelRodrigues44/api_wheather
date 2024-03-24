from django.db import models
from datetime import datetime

class WeatherModel(models.Model):
    id = models.IntegerField(primary_key=True, default='')
    temperature = models.FloatField()
    city = models.CharField(max_length=100, default='')
    atmosphericPressure = models.FloatField(default=0)
    humidity = models.FloatField(default=0)
    weather = models.CharField(max_length=100, default='')
    date = models.DateTimeField()

    @property
    def mongo_id_str(self):
        return str(self.id)

    def __str__(self):
        return f"Weather <{self.temperature}>"

    def __getattribute__(self, name):
        if name == 'date':
            return object.__getattribute__(self, name).strftime("%d/%m/%Y %H:%M:%S")
        elif name == '_id':
            return object.__getattribute__(self, 'id')
        else:
            return object.__getattribute__(self, name)