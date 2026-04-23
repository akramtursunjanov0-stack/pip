from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Film
from .serializers import (
    FilmListSerializer 
, FilmDetailSerializer , 
FilmValidateSerializer
)
from rest_framework.viewsets import ModelViewSet



class FilmViewSet(ModelViewSet):
    queryset =Film.objects.all()
    
    def get_serializer_class(self):
            if self.action == 'list':
                return FilmListSerializer
            return FilmDetailSerializer



@api_view(['GET','PUT','DELETE'])
def film_detail_api_view(request, id):
    try:
        film = Film.objects.get(id=id)
    except Film.DoesNotExist:
        return Response(data={'error':'film does not exist!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':     
        data = FilmDetailSerializer(film, many=False).data
        return Response(data=data)
    elif request.method == 'DELETE':
        film.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        film.title = request.data.get('title')
        film.text = request.data.get('text')
        film.release_year = request.data.get('release_year')
        film.rating = request.data.get('rating')
        film.is_hit = request.data.get('is_hit')
        film.director_id = request.data.get('director_id')
        film.genres.set(request.data.get('genres'))
        film.save()
        return Response(status=status.HTTP_201_CREATED)
    

@api_view(['GET', 'POST' ])
def film_list_api_view(request):
    if request.method == 'GET':
            
        films = Film.objects.select_related('director').prefetch_related('genres','reviews').all()
        data = FilmListSerializer(films, many=True).data
        return Response(
            data=data,
            status=status.HTTP_200_OK
        )
    elif request.method == 'POST':
        
        serializer = FilmValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)
        
        

        title = serializer.validated_data.get('title')
        text = serializer.validated_data.get('text')
        release_year = serializer.validated_data.get('release_year')
        rating = serializer.validated_data.get('rating')
        is_hit = serializer.validated_data.get('is_hit')
        director_id = serializer.validated_data.get('director_id')
        genres = serializer.validated_data.get('genres')



        film = Film.objects.create(
            title = title,
            text=text,
            release_year= release_year,
            rating=rating,
            is_hit=is_hit,
            director_id = director_id , 

        )

        film.genres.set(genres)
        film.save()


        return Response(status=status.HTTP_201_CREATED)
    


