from rest_framework import serializers
from .models import Director, Movie, Review
from rest_framework.serializers import ValidationError



class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = ['id', 'name', 'movies_count']

    def get_movies_count(self, obj):
        return obj.movie_set.count()

class DirectorValidationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    directors = serializers.IntegerField()
    list_directors = serializers.ListField(child=serializers.IntegerField())  # Указываем конкретное поле для child

    def validate_directors(self, directors):
        try:
            Director.objects.get(id=directors)
        except Director.DoesNotExist:
            raise ValidationError("Director does not exist")
        return directors

    def validate_list_directors(self, list_directors):
        directors_from_db = Director.objects.filter(id__in=list_directors)
        if len(directors_from_db) != len(list_directors):
            raise ValidationError("One or more directors do not exist in the list")
        return list_directors



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ReviewValidationSerializer(serializers.Serializer):
    review = serializers.IntegerField()
    list_reviews = serializers.ListField(child=serializers.CharField())

    def validate_list_reviews(self, list_reviews):
        reviews_from_db = Director.objects.filter(id__in=list_reviews)
        if len(reviews_from_db) != len(list_reviews):
            raise ValidationError("Reviews does not exists in list")
        return list_reviews


class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer(read_only=True)
    all_reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = 'title description director all_reviews rating'.split()
        depth = 1


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, max_length=100)
    director = serializers.CharField(required=True)
    description = serializers.CharField(required=False)
    duration = serializers.IntegerField()

