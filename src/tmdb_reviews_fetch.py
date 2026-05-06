import os
import requests
import pandas as pd
from dotenv import load_dotenv

from src.config import DATA_DIR, TMDB_POPULAR_URL

TMDB_REVIEWS_FILE = f"{DATA_DIR}/tmdb_reviews.csv"
MERGED_TMDB_IMDB_FILE = f"{DATA_DIR}/merged_tmdb_imdb.csv"
TMDB_REVIEW_MOVIE_LIMIT = 100

load_dotenv()


def get_reviews(movie_id):
    api_key = os.getenv("TMDB_API_KEY")

    if not api_key:
        raise ValueError("TMDB_API_KEY not found in .env file.")

    url = f"https://api.themoviedb.org/3/movie/{movie_id}/reviews"
    params = {"api_key": api_key}

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()
    results = data.get("results", [])

    reviews = []
    for review in results:
        reviews.append({
            "movie_id": movie_id,
            "content": review.get("content")
        })

    return reviews


def load_merged_movies():
    df = pd.read_csv(MERGED_TMDB_IMDB_FILE)
    return df


def fetch_reviews_for_movies(df, limit=TMDB_REVIEW_MOVIE_LIMIT):
    df = df.head(limit)

    all_reviews = []

    for _, row in df.iterrows():
        movie_id = row["id"]
        reviews = get_reviews(movie_id)
        all_reviews.extend(reviews)

    reviews_df = pd.DataFrame(all_reviews)
    return reviews_df


def save_reviews_data(reviews_df):
    reviews_df.to_csv(TMDB_REVIEWS_FILE, index=False)
    print(f"TMDb reviews saved to {TMDB_REVIEWS_FILE}")


def run_tmdb_reviews_pipeline():
    df = load_merged_movies()
    reviews_df = fetch_reviews_for_movies(df)

    print("Total reviews:", len(reviews_df))
    print(reviews_df.head())

    save_reviews_data(reviews_df)


if __name__ == "__main__":
    run_tmdb_reviews_pipeline()