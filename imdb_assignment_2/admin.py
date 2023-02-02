from django.contrib import admin

# Register your models here.
from imdb_assignment_2.models import Movie, Actor, Director, Cast, Rating

admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Cast)
admin.site.register(Rating)