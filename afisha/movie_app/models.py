from django.db import models

# Create your models here.

class Directo(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def rating(self):
        return 0


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.TextField()
    director = models.ForeignKey(Directo, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def rating(self):
        return 0


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    def rating(self):
        return 0
