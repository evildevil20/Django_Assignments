actors_list = [
    {
        "actor_id": "actor_1",
        "name": "Actor 1"
    },
    {
        "actor_id": "actor_2",
        "name": "Actor 2"
    },
    {
        "actor_id": "actor_3",
        "name": "Actor 3"
    },
    {
        "actor_id": "actor_4",
        "name": "Actor 4"
    },
    {
        "actor_id": "actor_5",
        "name": "Actor 5"
    },
    {
        "actor_id": "actor_6",
        "name": "Actor 6"
    }
]

directors_list = [
    "Director 1",
    "Director 2",
    "Director 3"
]

movies_list = [
    {
        "movie_id": "movie_1",
        "name": "Movie 1",
        "actors": [
            {
                "actor_id": "actor_1",
                "role": "hero",
                "is_debut_movie": False
            },
            {
                "actor_id": "actor_3",
                "role": "heroine",
                "is_debut_movie": True
            }
        ],
        "box_office_collection_in_crores": "12.3",
        "release_date": "2020-3-3",
        "director_name": "Director 1"
    },
    {
        "movie_id": "movie_2",
        "name": "Movie 2",
        "actors": [
            {
                "actor_id": "actor_4",
                "role": "hero",
                "is_debut_movie": False
            },
            {
                "actor_id": "actor_2",
                "role": "hero",
                "is_debut_movie": False
            }
        ],
        "box_office_collection_in_crores": "150.4",
        "release_date": "2021-7-19",
        "director_name": "Director 2"
    },
    {
        "movie_id": "movie_3",
        "name": "Movie 3",
        "actors": [
            {
                "actor_id": "actor_6",
                "role": "heroine",
                "is_debut_movie": False
            }
        ],
        "box_office_collection_in_crores": "20.8",
        "release_date": "2021-4-28",
        "director_name": "Director 3"
    },
    {
        "movie_id": "movie_4",
        "name": "Movie 4",
        "actors": [
            {
                "actor_id": "actor_3",
                "role": "heroine",
                "is_debut_movie": False
            },
            {
                "actor_id": "actor_5",
                "role": "hero",
                "is_debut_movie": False
            }
        ],
        "box_office_collection_in_crores": "200.8",
        "release_date": "2022-1-10",
        "director_name": "Director 2"
    },
    {
        "movie_id": "movie_5",
        "name": "Movie 5",
        "actors": [
            {
                "actor_id": "actor_1",
                "role": "hero",
                "is_debut_movie": False
            }
        ],
        "box_office_collection_in_crores": "175.4",
        "release_date": "2022-12-20",
        "director_name": "Director 1"
    }
]

movie_rating_list = [
    {
        "movie_id": "movie_1",
        "rating_one_count": 78,
        "rating_two_count": 45,
        "rating_three_count": 10,
        "rating_four_count": 80,
        "rating_five_count": 100
    },
    {
        "movie_id": "movie_2",
        "rating_one_count": 98,
        "rating_two_count": 15,
        "rating_three_count": 74,
        "rating_four_count": 37,
        "rating_five_count": 60
    },
    {
        "movie_id": "movie_3",
        "rating_one_count": 48,
        "rating_two_count": 79,
        "rating_three_count": 46,
        "rating_four_count": 73,
        "rating_five_count": 91
    },
    {
        "movie_id": "movie_4",
        "rating_one_count": 65,
        "rating_two_count": 70,
        "rating_three_count": 63,
        "rating_four_count": 100,
        "rating_five_count": 49
    },
    {
        "movie_id": "movie_5",
        "rating_one_count": 74,
        "rating_two_count": 95,
        "rating_three_count": 49,
        "rating_four_count": 37,
        "rating_five_count": 19
    }
]

input_movies_list = ["movie_6", "movie_3", "movie_5"]
