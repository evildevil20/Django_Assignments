from imdb_assignment_2.models import Actor, Director, Movie, Cast, Rating
from django.db.models import Count


# Task - 2
def add_actors(actors_list):
    actor_object = []
    for i in actors_list:
        actor_object.append(Actor(actor_id=i["actor_id"], name=i["name"]))
    Actor.objects.bulk_create(actor_object)


def add_directors(directors_list):
    director_object = []
    for i in directors_list:
        director_object.append(Director(name=i))
    Director.objects.bulk_create(director_object)


def add_movies(movies_list):
    movies_object = []
    for i in movies_list:
        movies_object.append(Movie(movie_id=i["movie_id"], name=i["name"],
                                   box_office_collection_in_crores=i["box_office_collection_in_crores"],
                                   release_date=i["release_date"], director_id=i["director_name"]))
    Movie.objects.bulk_create(movies_object)


def add_casts(movies_list):
    cast_object = []
    for i in movies_list:
        for j in i["actors"]:
            cast_object.append(
                Cast(actor_id=j["actor_id"],
                     movie_id=i["movie_id"],
                     role_name=j["role"],
                     is_debut_movie=j["is_debut_movie"]))
    Cast.objects.bulk_create(cast_object)


def add_ratings(movie_rating_list):
    rating_object = []
    for i in movie_rating_list:
        a = Movie.objects.get(movie_id=i["movie_id"])
        rating_object.append(Rating(movie=a, rating_one_count=i["rating_one_count"],
                                    rating_two_count=i["rating_two_count"], rating_three_count=i["rating_three_count"],
                                    rating_four_count=i["rating_four_count"], rating_five_count=i["rating_five_count"]))
    Rating.objects.bulk_create(rating_object)


# Task - 3
def get_no_of_distinct_movies_actor_acted(actor_id):
    answer = Actor.objects.filter(actor_id=actor_id).annotate(movies_count=Count('movie'))
    return answer.values()[0]['movies_count']


# Task - 4
def get_movies_directed_by_director(director_obj):
    answer = Director.objects.get(name=director_obj)
    return answer.movie_set.all()


# Task - 5
def get_average_rating_of_movie(movie_obj):
    try:
        answer = Rating.objects.get(movie=movie_obj)
        sum1 = \
            answer.rating_one_count * 1 + \
            answer.rating_two_count * 2 + \
            answer.rating_three_count * 3 + \
            answer.rating_four_count * 4 + \
            answer.rating_five_count * 5
        sum2 = \
            answer.rating_one_count + \
            answer.rating_two_count + \
            answer.rating_three_count + \
            answer.rating_four_count + \
            answer.rating_five_count
        print(format(sum1 / sum2, ".2f"))
    except:
        return 0


# Task - 6
def delete_movie_rating(movie_obj):
    answer = Rating.objects.get(movie_id=movie_obj)
    answer.delete()


# Task - 7
def get_all_actor_objects_acted_in_given_movies(input_movies_list):
    movie_actor_queryset = Movie.objects.all().prefetch_related('actor')
    answer = []
    index = 0
    movie_id_position_in_queryset = {}
    duplicate = {}
    for i in movie_actor_queryset:
        movie_id_position_in_queryset[i.movie_id] = index
        index += 1
    for movie_id in input_movies_list:
        actor_data = movie_actor_queryset[movie_id_position_in_queryset[movie_id]].acto.all()
        for actor in actor_data:
            if actor.actor_id not in duplicate:
                duplicate[actor.actor_id] = 1
                answer.append(actor)

    return answer


# Task - 8
def update_director_for_given_movie(movie_obj, director_obj):
    answer_movies = Movie.objects.get(movie_id=movie_obj)
    answer_director = Director.objects.get(name=director_obj)
    answer_movies.director = answer_director
    answer_movies.save()


# Task - 9
def get_distinct_movies_acted_by_actor_whose_name_contains_john():
    return Actor.objects.filter(name__contains='John')[0].movie_set.all()


# Task - 10
def remove_all_actors_from_given_movie(movie_obj):
    Movie.objects.get(movie_id=movie_obj).actor.clear()


# Task - 11
def get_all_rating_objects_for_given_movies(input_movies_list):
    answer = []
    for i in input_movies_list:
        try:
            b = Rating.objects.get(movie_id=i)
            answer.append({i: b})
        except Rating.DoesNotExist:
            b = None

    return answer
