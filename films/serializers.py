from django.utils import timezone
from rest_framework import serializers
from .models import Film , Director
from rest_framework.exceptions import ValidationError

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id fio'.split()



class FilmDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film 
        fields = '__all__'




class FilmListSerializer(serializers.ModelSerializer):
    director = DirectorSerializer(many=False) 
    genres = serializers.SerializerMethodField()

    class Meta:
        model = Film 
        fields = 'director genres id title rating release_year reviews'.split()
        depth = 1 

    def get_genres(self, film):
        return film.genre_names()[0:2]
    
class FilmValidateSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, max_length=255, min_length=3)
    text = serializers.CharField(required=False)
    release_year = serializers.IntegerField(min_value=1900, max_value=timezone.now().year + 10)
    rating = serializers.FloatField(min_value=1, max_value=10)
    is_hit = serializers.BooleanField()
    director_id = serializers.IntegerField()
    genres = serializers.ListField(child=serializers.IntegerField())

    def validate(self, attrs):
        director_id = attrs.get('director_id')
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError('Director does not exist')
        return attrs