import os
import csv
import requests
from dotenv import load_dotenv

from src.config import TMDB_POPULAR_URL, TMDB_MOVIES_FILE, TMDB_TOTAL_PAGES

load_dotenv()


def get_popular_movies_page(page=1):
    api_key = os.getenv("TMDB_API_KEY")

    if not api_key:
        raise ValueError("TMDB_API_KEY not found in .env file.")

    params = {
        "api_key": api_key,
        "language": "en-US",
        "page": page
    }

    response = requests.get(TMDB_POPULAR_URL, params=params)
    response.raise_for_status()

    data = response.json()
    return data["results"]


def get_popular_movies_multiple_pages(total_pages=TMDB_TOTAL_PAGES):
    all_movies = []

    for page in range(1, total_pages + 1):
        print(f"Fetching TMDb page {page}...")
        movies = get_popular_movies_page(page)

        for movie in movies:
            movie_info = {
                "id": movie.get("id"),
                "title": movie.get("title"),
                "vote_average": movie.get("vote_average"),
                "vote_count": movie.get("vote_count"),
                "release_date": movie.get("release_date"),
                "popularity": movie.get("popularity"),
                "genre_ids": movie.get("genre_ids")
            }
            all_movies.append(movie_info)

    return all_movies


def save_movies_to_csv(movies, filename=TMDB_MOVIES_FILE):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "id",
                "title",
                "vote_average",
                "vote_count",
                "release_date",
                "popularity",
                "genre_ids"
            ]
        )

        writer.writeheader()
        writer.writerows(movies)


def run_tmdb_pipeline():
    movies = get_popular_movies_multiple_pages()
    print(f"Total TMDb movies collected: {len(movies)}")

    save_movies_to_csv(movies)
    print(f"TMDb data saved to {TMDB_MOVIES_FILE}")


if __name__ == "__main__":
    run_tmdb_pipeline()