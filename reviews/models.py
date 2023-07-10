from django.db import models
from utils.models import AbstractModel

# Create your models here.
class Business(AbstractModel):
    google_id = models.CharField(max_length=100)
    place_id = models.CharField(max_length=100)
    name = models.CharField(max_length=256)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    rating = models.FloatField()

    def __str__(self):
        return self.name

class Review(AbstractModel):
    google_id = models.CharField(max_length=100)
    author_name = models.CharField(max_length=120)
    rating = models.FloatField()
    text = models.TextField()
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.text
    
class BusinessRegisterStage(AbstractModel):
   url = models.TextField()