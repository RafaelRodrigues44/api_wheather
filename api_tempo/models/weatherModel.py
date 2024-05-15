from django.db import models

class WeatherModel(models.Model):
    id = models.IntegerField(primary_key=True)
    temperature = models.FloatField()
    city = models.CharField(max_length=100)
    atmosphericPressure = models.FloatField(default=0)
    humidity = models.FloatField(default=0)
    weather = models.CharField(max_length=100)
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
        elif name == 'city':
            return object.__getattribute__(self, 'city')
        else:
            return super().__getattribute__(name)
