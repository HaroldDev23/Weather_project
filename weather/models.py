from django.db import models
from datetime import datetime

# Create your models here.
class WeatherData(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    precipitation = models.FloatField()
    wind_speed = models.FloatField()
    uv = models.FloatField()
    pressure = models.FloatField()
    evapotranspiration = models.FloatField()
    temperation_soil = models.FloatField()
    couverture = models.FloatField()
    date = models.DateField(auto_now_add=True)
    
class WeatherPredict(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    precipitation = models.FloatField()
    wind_speed = models.FloatField()
    uv = models.FloatField()
    pressure = models.FloatField()
    evapotranspiration = models.FloatField()
    temperation_soil = models.FloatField()
    couverture = models.FloatField()
    rose = models.FloatField()
    date = models.DateField(auto_now_add=True)
