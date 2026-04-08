import os
import requests
from dotenv import load_dotenv

load_dotenv()


def get_popular_movies():
    api_key = os.getenv("TMDB_API_KEY")

    url = "https://api.themoviedb.org/3/movie/popular"
    params = {
        "api_key": api_key,
        "language": "en-US",
        "page": 1
    }

    response = requests.get(url, params=params)
    data = response.json()

    return data["results"]


if __name__ == "__main__":
    movies = get_popular_movies()

    for movie in movies[:5]:
        print(movie["title"], movie["vote_average"])