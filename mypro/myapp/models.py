from django.db import models

# Create your models here.
class Gallery(models.Model):
    classimages=models.ImageField(upload_to='images/')
    