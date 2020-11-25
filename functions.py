import yaml
from classes import Game, User


def get_data(filename):
    with open(filename, "r") as stream:
        yaml_data = yaml.load(stream, Loader=yaml.FullLoader)
        return yaml_data


def make_collection(data, games_collection=None, genre_tags=None):
    if games_collection is None:
        games_collection = []
    if genre_tags is None:
        genre_tags = []

    for item in data:
        if data[item].get("age_rating"):
            games_collection.append(Game(item, data[item], genre_tags))
        else:
            make_collection(data[item], games_collection, genre_tags+[item])
    return games_collection


def get_users():
    data = get_data("users.yml")
    users = []

    for username in data:
        users.append(User(username, data[username]))

    return users
