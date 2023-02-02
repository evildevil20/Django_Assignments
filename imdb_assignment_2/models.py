# Create your models here.
from django.db import models


class Actor(models.Model):
    actor_id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return f"actor_id:{self.actor_id},name:{self.name}"


class Director(models.Model):
    name = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=100)
    movie_id = models.CharField(max_length=100, primary_key=True)
    release_date = models.DateField()
    box_office_collection_in_crores = models.FloatField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, blank=False)
    actor = models.ManyToManyField(Actor, through='Cast')

    def __str__(self):
        return f"name:{self.name}," \
               f"movie_id:{self.movie_id}," \
               f"release_date:{self.release_date}," \
               f"director:{self.director},"\
               f"box_office:{self.box_office_collection_in_crores}"


class Cast(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    role_name = models.CharField(max_length=100)
    is_debut_movie = models.BooleanField(default=False)


class Rating(models.Model):
    movie = models.OneToOneField(Movie, on_delete=models.CASCADE, primary_key=True)
    rating_one_count = models.IntegerField(default=0)
    rating_two_count = models.IntegerField(default=0)
    rating_three_count = models.IntegerField(default=0)
    rating_four_count = models.IntegerField(default=0)
    rating_five_count = models.IntegerField(default=0)

    def __str__(self):
        return f"movie_id:{self.movie}," \
               f"rating_one_count:{self.rating_one_count}," \
               f"rating_two_count:{self.rating_two_count}," \
               f"rating_three_count:{self.rating_three_count}," \
               f"rating_four_count:{self.rating_four_count}," \
               f"rating_five_count:{self.rating_five_count}"
