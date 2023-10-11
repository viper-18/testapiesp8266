from django.db import models

# Create your models here.
class Movie(models.Model):
    status = models.CharField(max_length=50)
    time = models.CharField(max_length=200)

    def __str__(self):
        return self.name