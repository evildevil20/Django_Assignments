from __future__ import unicode_literals

from django.db import models


class Actor(models.Model):
    actor_id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    movie_id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    actors = models.ManyToManyField(Actor, through='Cast')
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    release_date = models.DateField()
    box_office_collection_in_crores = models.FloatField()

    def __str__(self):
        return f"name:{self.name}," \
               f"movie_id:{self.movie_id}," \
               f"release_date:{self.release_date}," \
               f"director:{self.director}," \
               f"box_office:{self.box_office_collection_in_crores}"


class Cast(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)
    is_debut_movie = models.BooleanField(default=False)

    def __str__(self):
        return self.role


class Rating(models.Model):
    movie = models.OneToOneField(Movie, on_delete=models.CASCADE)
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
