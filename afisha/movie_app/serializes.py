from rest_framework import serializers
from .models import Director, Movie, Review


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.IntegerField()
    class Meta:
        model = Director
        fields = '__all__'


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

