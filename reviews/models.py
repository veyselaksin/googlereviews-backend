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
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    google_id = models.CharField(max_length=100)
    author_name = models.CharField(max_length=120)
    author_url = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    rating = models.IntegerField()
    text = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.text
    
class BusinessRegisterStage(AbstractModel):
   url = models.TextField()