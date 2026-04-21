from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Film
from .serializers import FilmListSerializer , FilmDetailSerializer




@api_view(['GET'])
def film_detail_api_view(request, id):
    try:
        film = Film.objects.get(id=id)
    except Film.DoesNotExist:
        return Response(data={'error':'film does not exist!'},
                        status=status.HTTP_404_NOT_FOUND)
    
    data = FilmDetailSerializer(film, many=False).data
    return Response(data=data)


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
        return Response()
    


