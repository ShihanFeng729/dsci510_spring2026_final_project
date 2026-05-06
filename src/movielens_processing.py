import pandas as pd

from src.config import DATA_DIR

MOVIELENS_RATINGS_FILE = f"{DATA_DIR}/ratings.dat"
MOVIELENS_MOVIES_FILE = f"{DATA_DIR}/movies.dat"
MOVIELENS_CLEANED_FILE = f"{DATA_DIR}/movielens_cleaned.csv"


def load_movielens_ratings():
    ratings = pd.read_csv(
        MOVIELENS_RATINGS_FILE,
        sep="::",
        engine="python",
        names=["userId", "movieId", "rating", "timestamp"]
    )
    return ratings


def load_movielens_movies():
    movies = pd.read_csv(
        MOVIELENS_MOVIES_FILE,
        sep="::",
        engine="python",
        encoding="latin-1",
        names=["movieId", "title_with_year", "genres"]
    )
    return movies


def clean_movielens_data(ratings, movies):
    print("Ratings shape:", ratings.shape)
    print("Movies shape:", movies.shape)

    movie_stats = ratings.groupby("movieId").agg(
        movielens_rating=("rating", "mean"),
        movielens_votes=("rating", "count")
    ).reset_index()

    print("Movie stats shape:", movie_stats.shape)

    merged = pd.merge(movie_stats, movies, on="movieId")
    print("After merge:", merged.shape)

    merged["year"] = merged["title_with_year"].str.extract(r"\((\d{4})\)$")
    merged["year"] = pd.to_numeric(merged["year"], errors="coerce")

    merged = merged.dropna(subset=["year"])

    merged["title"] = merged["title_with_year"].str.replace(r"\s*\(\d{4}\)$", "", regex=True)
    merged["title"] = merged["title"].str.lower()
    merged["year"] = merged["year"].astype(int)

    merged = merged[[
        "movieId",
        "title",
        "year",
        "movielens_rating",
        "movielens_votes"
    ]]

    return merged


def save_movielens_data(data):
    data.to_csv(MOVIELENS_CLEANED_FILE, index=False)
    print(f"MovieLens data saved to {MOVIELENS_CLEANED_FILE}")


def run_movielens_pipeline():
    ratings = load_movielens_ratings()
    movies = load_movielens_movies()

    cleaned_data = clean_movielens_data(ratings, movies)
    print("Final cleaned MovieLens shape:", cleaned_data.shape)
    print(cleaned_data.head())

    save_movielens_data(cleaned_data)


if __name__ == "__main__":
    run_movielens_pipeline()