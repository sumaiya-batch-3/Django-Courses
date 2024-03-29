from django.db import models

# Create your models here.
class CarUser(models.Model):
    name = models.CharField( max_length=50)
    email = models.EmailField()
    phone_no = models.CharField(max_length=12)
    image = models.ImageField(upload_to='user/media/uploads/', blank = True, null = True)