from django.db import models
from musicians.models import Musician


class Album(models.Model):
    album_name = models.CharField(max_length=200)
    release_date = models.DateField()
    rating = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]
    album_rating = models.CharField(max_length=6, choices=rating)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.album_name