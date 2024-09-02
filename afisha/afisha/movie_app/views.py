from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Directo, Movie, Review
from rest_framework import status

from .serializes import DirectoSerializer, MovieSerializer, ReviewSerializer


@api_view(http_method_names=['GET'])
def directors_list_api_view(request):
    directos = Directo.objects.all()
    lista_directos = DirectoSerializer(instance=directos, many=True).data
    return Response(data=lista_directos, status=status.HTTP_200_OK)

@api_view(['GET'])
def directors_detail_api_view(request, id):
    try:
        directo = Directo.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Directo not found'})
    data = DirectoSerializer(directo).data
    return Response(data=data)


@api_view(http_method_names=['GET'])
def movies_list_api_view(request):
    movies = Movie.objects.all()
    lista_movies = MovieSerializer(instance=movies, many=True).data
    return Response(data=lista_movies, status=status.HTTP_200_OK)

@api_view(['GET'])
def movies_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Movie not found'})
    data = MovieSerializer(movie).data
    return Response(data=data)

@api_view(http_method_names=['GET'])
def reviews_list_api_view(request):
    reviews = Review.objects.all()
    lista_reviews = ReviewSerializer(instance=reviews, many=True).data
    return Response(data=lista_reviews, status=status.HTTP_200_OK)

@api_view(['GET'])
def reviews_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Review not found'})
    data = ReviewSerializer(review).data
    return Response(data=data)