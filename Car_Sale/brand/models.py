from django.db import models

# Create your models here.
class Brand(models.Model):
    b_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100,unique = True, null = True,blank= True)
    def __str__(self):
     return self.b_name