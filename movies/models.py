from django.db import models

# Create your models here.

class Rating(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    alt_name = models.CharField(max_length=200, blank=True)
    year = models.IntegerField(blank=True, null=True)
    imdb_rating = models.FloatField(max_length=3, blank=True, null=True)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    date_watched = models.DateField(blank=True, null=True)
    imdb_id = models.CharField(max_length=30, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name
