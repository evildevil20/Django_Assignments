from imdb_assignment_5.models import Actor, Director, Movie, Cast, Rating
from typing import *


# Task 1
def add_actors(actors_list: List[Dict[str, str]]) -> None:
    actor_object = []
    for i in actors_list:
        actor_object.append(Actor(actor_id=i["actor_id"], name=i["name"], gender=i["gender"]))
    Actor.objects.bulk_create(actor_object)


def add_directors(directors_list: List[str]) -> None:
    director_object = []
    for i in directors_list:
        director_object.append(Director(name=i))
    Director.objects.bulk_create(director_object)


def add_movies(movies_list) -> None:
    movies_object = []
    for i in movies_list:
        movies_object.append(Movie(movie_id=i["movie_id"], name=i["name"],
                                   box_office_collection_in_crores=i["box_office_collection_in_crores"],
                                   release_date=i["release_date"], director_id=i["director_name"]))
    Movie.objects.bulk_create(movies_object)


def add_casts(movies_list) -> None:
    cast_object = []
    for i in movies_list:
        for j in i["actors"]:
            cast_object.append(
                Cast(actor_id=j["actor_id"],
                     movie_id=i["movie_id"],
                     role=j["role"],
                     is_debut_movie=j["is_debut_movie"]))
    Cast.objects.bulk_create(cast_object)


def add_ratings(movie_rating_list: Dict) -> None:
    rating_object = []
    for i in movie_rating_list:
        a = Movie.objects.get(movie_id=i["movie_id"])
        rating_object.append(Rating(movie=a, rating_one_count=i["rating_one_count"],
                                    rating_two_count=i["rating_two_count"], rating_three_count=i["rating_three_count"],
                                    rating_four_count=i["rating_four_count"], rating_five_count=i["rating_five_count"]))
    Rating.objects.bulk_create(rating_object)


# Task 2
def remove_all_actors_from_given_movie(movie_obj) -> None:
    Movie.objects.get(movie_id=movie_obj.movie_id).actors.clear()


# Task 3
def get_all_rating_objects_for_given_movies(movie_objs) -> Rating:
    list_of_movie_ids = []
    answer: Rating = []
    for movie in movie_objs:
        list_of_movie_ids.append(movie.movie_id)
    movies = Movie.objects.filter(movie_id__in=list_of_movie_ids)
    for i in movies:
        answer.append(Rating.objects.get(movie=i.movie_id))
    return answer


def get_total_rating_for_given_movie_names(movie_names: List[str]) -> Dict[str, int]:
    movie_rating_queryset = Movie.objects.prefetch_related('rating')
    answer: Dict[str, int] = {}
    movie_name_position_in_queryset: Dict[str, int] = {}
    index = 0
    for i in movie_rating_queryset:
        movie_name_position_in_queryset[i.name] = index
        index += 1
    for movie in movie_names:
        temp = movie_rating_queryset[movie_name_position_in_queryset[movie]].rating
        total = \
            temp.rating_one_count + \
            temp.rating_two_count + \
            temp.rating_three_count + \
            temp.rating_four_count + \
            temp.rating_five_count
        answer[movie] = total
    return answer


# Task 4
def get_movies_by_given_movie_names(movie_names: List[str]):
    movie_actor_queryset = Movie.objects.all().prefetch_related('actors')
    movie_director_queryset = Movie.objects.all().prefetch_related('director')
    cast = Cast.objects.all().select_related('movie').select_related('actor')
    movie_rating = get_total_rating_for_given_movie_names(movie_names)
    answer = []
    movie_names_position_in_queryset1: Dict[str, int] = {}
    movie_names_position_in_queryset2: Dict[str, int] = {}
    movie_names_position_in_queryset3: Dict[str, int] = {}
    index: int = 0
    for i in movie_actor_queryset:
        movie_names_position_in_queryset1[i.name] = index
        index += 1
    index = 0
    for i in movie_director_queryset:
        movie_names_position_in_queryset2[i.name] = index
        index += 1
    index = 0
    for i in cast:
        if i.movie.name not in movie_names_position_in_queryset3:
            movie_names_position_in_queryset3[i.movie.name] = []
        movie_names_position_in_queryset3[i.movie.name].append(index)
        index += 1
    for movie in movie_names:
        temp = dict()
        temp["movie_id"] = movie_actor_queryset[movie_names_position_in_queryset1[movie]].movie_id
        temp["name"] = movie_actor_queryset[movie_names_position_in_queryset1[movie]].name
        cast_list = []
        for i in movie_names_position_in_queryset3[movie]:
            cast_list.append({"actor": {"name": cast[i].actor.name, "actor_id": cast[i].actor.actor_id,
                                        "gender": cast[i].actor.gender},
                              "role": cast[i].role, "is_debut_movie": cast[i].is_debut_movie})
        temp["cast"] = cast_list
        temp["release_date"] = movie_actor_queryset[
            movie_names_position_in_queryset1[movie]].release_date
        temp["box_office_collection_in_crores"] = movie_actor_queryset[
            movie_names_position_in_queryset1[movie]].box_office_collection_in_crores
        temp["director_name"] = movie_director_queryset[movie_names_position_in_queryset2[movie]].director
        temp["average_rating"] = round(movie_rating[movie] / 5, 1)
        temp["total_number_of_ratings"] = movie_rating[movie]
        answer.append(temp)
    return answer


# Task 5
def get_all_actor_objects_acted_in_given_movies(movie_objs):
    movie_actor_queryset = Movie.objects.all().prefetch_related('actors')
    answer = []
    movie_ids = []
    movie_id_position_in_queryset = {}
    duplicate = {}
    index = 0
    for a in movie_objs:
        movie_ids.append(a.movie_id)
    for i in movie_actor_queryset:
        movie_id_position_in_queryset[i.movie_id] = index
        index += 1
    for movie_id in movie_ids:
        actor_data = movie_actor_queryset[movie_id_position_in_queryset[movie_id]].actors.all()
        for j in actor_data:
            if j.actor_id not in duplicate:
                duplicate[j.actor_id] = 1
                answer.append(j)

    return answer


# Task 6
def get_female_cast_details_from_movies_having_more_than_five_female_cast():
    movie_queryset = Movie.objects.all()
    movie_names = []
    for movie in movie_queryset:
        movie_names.append(movie.name)
    data = get_movies_by_given_movie_names(movie_names)
    answer = []
    for i in data:
        count = 0
        for j in i["cast"]:
            if j["actor"]["gender"] == "FEMALE":
                count += 1
        if count >= 5:
            answer.append(i)

    return answer


# Task 7
def get_actor_movies_released_in_year_greater_than_or_equal_to_2000():
    movie_queryset = Movie.objects.all()
    movie_names = []
    for i in movie_queryset:
        movie_names.append(i.name)
    data = get_movies_by_given_movie_names(movie_names)
    index_of_actor = {}
    answer = []
    index: int = 0
    for i in data:
        if i["release_date"].year >= 2000:
            for j in i["cast"]:
                if j["actor"]["name"] in index_of_actor:
                    index = index_of_actor[j["actor"]["name"]]
                    answer[index]["movies"].append({"movie_id": i["movie_id"], "name": i["name"],
                                                    "cast": {"role": j["role"], "is_debut_movie": j["is_debut_movie"],
                                                             "box_office_collection_in_crores": i[
                                                                 "box_office_collection_in_crores"],
                                                             "release_date": i["release_date"],
                                                             "director_name": i["director_name"],
                                                             "average_rating": i["average_rating"],
                                                             "total_number_of_ratings": i["total_number_of_ratings"]}})
                else:
                    index_of_actor[j["actor"]["name"]] = index
                    index += 1
                    temp = {"name": j["actor"]["name"], "actor_id": j["actor"]["actor_id"],
                            "movies": [{"movie_id": i["movie_id"], "name": i["name"],
                                        "cast": {"role": j["role"], "is_debut_movie": j["is_debut_movie"]},
                                        "box_office_collection_in_crores": i[
                                            "box_office_collection_in_crores"], "release_date": i["release_date"],
                                        "director_name": i["director_name"],
                                        "average_rating": i["average_rating"],
                                        "total_number_of_ratings": i["total_number_of_ratings"]}]}
                    answer.append(temp)
    return answer


# Task 8
def reset_ratings_for_movies_in_given_year(year: int) -> None:
    movies = Movie.objects.filter(release_date__year=year)
    movies_id_list = []
    for i in movies:
        movies_id_list.append(i.movie_id)
    answer = Rating.objects.filter(movie__in=movies_id_list)
    for i in answer:
        i.rating_one_count = 0
        i.rating_two_count = 0
        i.rating_three_count = 0
        i.rating_four_count = 0
        i.rating_five_count = 0
        i.save()
