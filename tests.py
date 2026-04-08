from src.tmdb_api import get_popular_movies


if __name__ == "__main__":
    print("Running tests for final project...")

    movies = get_popular_movies()

    print(f"Number of movies returned: {len(movies)}")
    print("First 3 movies:")

    for movie in movies[:3]:
        print({
            "title": movie["title"],
            "vote_average": movie["vote_average"],
            "release_date": movie["release_date"]
        })