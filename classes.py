from random import randint


class Game(object):
    def __init__(self, name, dict_info, genre_tags):
        self.name = dict_info.get("name", name)
        self.age_rating = int(dict_info.get("age_rating"))
        self.avg_duration = int(dict_info.get("avg_duration"))
        self.user_rating = 0
        self.max_players = int(dict_info.get("max_players"))
        self.out_of_stack = bool(dict_info.get("out_of_stack"))
        self.min_cost = int(dict_info.get("min_cost"))
        self.year = int(dict_info.get("year"))
        self.company = dict_info.get("company")
        self.genre_tags = genre_tags

    def __str__(self):
        return self.name


class User(object):
    def __init__(self, name, dict_info):
        self.name = name
        self.age = dict_info.get("age")
        self.ratings = dict_info.get("ratings", dict())

    def __str__(self):
        return self.name

    def generate_ratings(self, product_count):
        ratings = []

        for product in range(product_count):
            ratings.append(randint(0, 100)/100)

        self.ratings = ratings

    def set_rating(self, product_id, new_rating):
        self.ratings[product_id] = new_rating

    def get_rating(self, product_id):
        return self.ratings[product_id]

    def get_ratings_count(self):
        return len(self.ratings)


class RatingTable(object):
    def __init__(self, game_list, user_list):
        self.users = user_list
        self.games = game_list
        self.table = [user.ratings for user in user_list]
