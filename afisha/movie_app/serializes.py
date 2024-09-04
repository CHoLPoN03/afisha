from rest_framework import serializers
from .models import Directo, Movie, Review


class DirectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Directo
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'




