from django.db import models
# from album_app.models import AlbumInfo

# Create your models here.
class Musician(models.Model):
    first_Name = models.CharField(max_length=200, default=None)
    last_Name = models.CharField(max_length=200, default=None)
    email = models.EmailField(default=None)
    phone_number = models.IntegerField(default=None)
    Instrument_type = models.CharField(max_length=200, default=None)
    # album = models.ManyToManyField(AlbumInfo)pymanage.py

    def __str__(self):
        return f"{self.first_Name} {self.last_Name}"
  
  