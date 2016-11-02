from django.db import models


# Create your models here.
class car_id(models.Model):
    Trip = models.CharField(max_length=10)


class car_details(models.Model):
    Trip_name = models.ForeignKey(car_id, on_delete=models.CASCADE)
    Status = models.CharField(max_length=10, null=True)
    TimeDate = models.DateTimeField(null=True)
    Map = models.URLField(max_length=20, null=True)
    Lat = models.FloatField(null=True)
    Long = models.FloatField(null=True)
