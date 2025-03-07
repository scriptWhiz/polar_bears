from django.db import models
from django.utils import timezone

# Create your models here.

class Bear(models.Model):
    bearID = models.IntegerField()
    pTT_ID = models.IntegerField()
    capture_lat = models.FloatField()
    capture_long = models.FloatField()
    sex = models.TextField()
    age_class = models.TextField()
    ear_applied = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

#We join all of the attributes into a string so that data can be shared by models 
#in foreign keys, and to ensure the relevant parts can be displayed.

    def __str__(self):
        return f'{self.id}, {self.bearID}, {self.pTT_ID}, {self.capture_lat}, {self.capture_long},{self.sex}, {self.age_class}, {self.ear_applied}, {self.created_date}'
 
    def female():
        females = Bear.objects.filter(sex='F')
        return females

class Sighting(models.Model):
            bear_id = models.ForeignKey('bears.Bear', on_delete=models.CASCADE, related_name='sightings')
            deploy_id = models.IntegerField(default=None)
            recieved = models.TextField()
            latitude = models.FloatField()
            longitude = models.FloatField()
            temperature = models.FloatField()
            created_date=models.DateTimeField(auto_now_add=True)

            def __str__(self):
                    return f'{self.bear_id}, {self.deploy_id}, {self.recieved}, {self.latitude}, {self.longitude}, {self.temperature}, {self.created_date}'