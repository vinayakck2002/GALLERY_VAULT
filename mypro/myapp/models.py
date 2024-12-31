from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Gallery(models.Model):
    classimages=models.ImageField(upload_to='images/')
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    