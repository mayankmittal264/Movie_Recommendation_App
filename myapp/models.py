from django.db import models


# Create your models here.
class Movie(models.Model):
    Movie_title = models.CharField(max_length=30, unique=True)
    genre = models.TextField(max_length=100)
    keywords = models.TextField(max_length=100)
    image = models.ImageField(upload_to='poster/')

    def __str__(self):
        return self.Movie_title
