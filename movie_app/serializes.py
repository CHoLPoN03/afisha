from rest_framework import serializers
from .models import Director, Movie, Review



class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = ['id', 'name', 'movies_count']

    def get_movies_count(self, obj):
        return obj.movie_set.count()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer(read_only=True)
    all_reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = 'title description director all_reviews rating'.split()
        depth = 1

