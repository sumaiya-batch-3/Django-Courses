from django.db import models

# Create your models here.

class Musician(models.Model):
    first_name = models.CharField(max_length=200, default=None)
    last_name = models.CharField(max_length=200, default=None)
    email = models.EmailField(default=None)
    phone_number = models.IntegerField(default=None)
    instrument_type = models.CharField(max_length=200, default=None)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'