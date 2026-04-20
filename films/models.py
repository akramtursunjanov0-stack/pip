from django.db import models

class Director(models.Model):
    fio = models.CharField(max_length=100)
    birthday = models.DateField()

    def  __str__(self):
       return self.fio 


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name




class Film(models.Model):
    director = models.ForeignKey(Director, on_delete=models.CASCADE,null=True)
    genres = models.ManyToManyField(Genre, blank=True)
    title = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)
    release_year = models.IntegerField()
    rating = models.FloatField()
    is_hit = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

    def genre_names(self):
        return [i.name for i in self.genres.all()]

