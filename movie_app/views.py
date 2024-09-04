from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Director, Movie, Review
from rest_framework import status

from .serializes import DirectorSerializer, MovieSerializer, ReviewSerializer


@api_view(http_method_names=['GET', 'POST'])
def directors_list_create_api_view(request):
    if request.method == 'GET':
        directors = Director.objects.annotate(movies_count=Count('movie'))
        lista_directos =DirectorSerializer(instance=directors, many=True).data
        return Response(data=lista_directos, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        name = request.data.get('name')
        directors = Director.objects.create(name=name)
        lista_directors =DirectorSerializer(instance=directors).data

        return Response(data=lista_directors, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def directors_detail_api_view(request, id):
    try:
        directo = Director.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Directo not found'})

    if request.method == 'GET':
        data =DirectorSerializer(directo).data
        return Response(data=data)

    elif request.method == 'PUT':
        directo.name = request.data.get('name')
        directo.save()
        return Response(DirectorSerializer(directo).data, status=status.HTTP_201_CREATED)

    elif request.method == 'DELETE':
        directo.delete()
        return Response(DirectorSerializer(directo).data, status=status.HTTP_404_NOT_FOUND)


@api_view(http_method_names=['GET', 'POST'])
def movies_list_create_api_view(request):
    if request.method == 'GET':
        movies = Movie.objects.select_related('director').prefetch_related(
            'all_reviews',
        ).all()
        lista_movies = MovieSerializer(instance=movies, many=True).data
        return Response(data=lista_movies, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        title = request.data.get('title')
        director_id = request.data.get('director_id')
        description = request.data.get('description', 'No text')
        duration = request.data.get('duration')

        try:
            director = Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            return Response({"error": "Director not found"}, status=status.HTTP_404_NOT_FOUND)


        movie = Movie.objects.create(
            title=title,
            director=director,
            description=description,
            duration=duration
        )
        return Response(data=MovieSerializer(movie).data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT', 'DELETE'])
def movies_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Movie not found'})

    if request.method == 'GET':
        data = MovieSerializer(movie).data
        return Response(data=data)

    elif request.method == 'PUT':
        movie.title = request.data.get('title')
        director_id = request.data.get('director_id')

        try:
            director = Director.objects.get(id=director_id)
        except:
            return Response()

        movie.director = director
        movie.duration = request.data.get('duration')
        movie.description = request.data.get('description')
        movie.save()
        return Response(data=MovieSerializer(movie).data, status=status.HTTP_201_CREATED)

    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(http_method_names=['GET', 'POST'])
def reviews_list_create_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        lista_reviews = ReviewSerializer(instance=reviews, many=True).data
        return Response(data=lista_reviews, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        text = request.data.get('text')
        stars = request.data.get('stars')
        movie_id = request.data.get('movie_id')

        review = Review.objects.create(
            text=text,
            stars=stars,
            movie_id=movie_id
        )
        return Response(ReviewSerializer(review).data, status=status.HTTP_201_CREATED)



@api_view(['GET', 'PUT', 'DELETE'])
def reviews_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Review not found'})
    if request.method == 'GET':
        data = ReviewSerializer(review).data
        return Response(data=data)

    elif request.method == 'PUT':
        review.text = request.data.get('text')
        review.stars = request.data.get('stars')
        review.movie_id = request.data.get('movie_id')
        review.save()
        return Response(ReviewSerializer(review).data, status=status.HTTP_201_CREATED)

    elif request.method == 'DELETE':
        review.delete()
        return Response(ReviewSerializer(review).data, status=status.HTTP_204_NO_CONTENT)