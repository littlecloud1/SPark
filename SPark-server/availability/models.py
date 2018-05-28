from django.db import models


class Spot(models.Model):
    spotID=models.CharField(max_length=200)
    currentCar=models.CharField(max_length=20)
    position=models.CharField(max_length=200)
    isAvailableNow=models.BooleanField(default=True)

class AvailableTime(models.Model):
    spot=models.ForeignKey(Spot,on_delete=models.CASCADE)

    # every interval is 30 minutes there are total 24 hours therefore 48
    for i in range(48):
        exec('slot'+str(i)+'=models.BooleanField(default=True)')