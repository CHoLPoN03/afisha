from django.db import models


# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def rating(self):
        return 0


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.TextField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def rating(self):
        reviews = self.all_reviews.all()
        if reviews:
            total_stars = sum(review.stars for review in reviews)
            return total_stars / reviews.count()
        return 0


STAR_CHOICES = (
    (1, '*'),
    (2, '**'),
    (3, '***'),
    (4, '****'),
    (5, '*****')
)


class Review(models.Model):
    text = models.TextField()
    stars = models.IntegerField(choices=STAR_CHOICES, default=5)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='all_reviews')


    def __str__(self):
        return self.text

    def rating(self):
        return 0
