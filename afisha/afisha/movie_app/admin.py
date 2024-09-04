from django.contrib import admin

from movie_app.models import Directo, Movie, Review

# Register your models here.

admin.site.register(Directo)
admin.site.register(Movie)
admin.site.register(Review)