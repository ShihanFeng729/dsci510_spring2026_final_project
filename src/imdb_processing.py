import pandas as pd

from src.config import (
    IMDB_BASICS_FILE,
    IMDB_RATINGS_FILE,
    IMDB_CLEANED_FILE,
    IMDB_MIN_VOTES
)


def load_imdb_basics():
    basics = pd.read_csv(IMDB_BASICS_FILE, sep="\t", low_memory=False)
    return basics


def load_imdb_ratings():
    ratings = pd.read_csv(IMDB_RATINGS_FILE, sep="\t", low_memory=False)
    return ratings


def clean_imdb_data(basics, ratings):
    print("Original basics:", basics.shape)
    print("Original ratings:", ratings.shape)

    basics = basics[basics["titleType"] == "movie"]
    print("After filtering movies:", basics.shape)

    basics = basics[basics["startYear"] != "\\N"]
    basics["startYear"] = basics["startYear"].astype(int)

    basics = basics[["tconst", "primaryTitle", "startYear"]]

    merged = pd.merge(basics, ratings, on="tconst")
    print("After merge:", merged.shape)

    merged = merged[merged["numVotes"] > IMDB_MIN_VOTES]
    print("After filtering by votes:", merged.shape)

    merged = merged.rename(columns={
        "primaryTitle": "title",
        "startYear": "year",
        "averageRating": "imdb_rating",
        "numVotes": "imdb_votes"
    })

    return merged


def save_imdb_data(data):
    data.to_csv(IMDB_CLEANED_FILE, index=False)
    print(f"IMDb data saved to {IMDB_CLEANED_FILE}")


def run_imdb_pipeline():
    basics = load_imdb_basics()
    ratings = load_imdb_ratings()

    cleaned_imdb = clean_imdb_data(basics, ratings)
    print(cleaned_imdb.head())

    save_imdb_data(cleaned_imdb)


if __name__ == "__main__":
    run_imdb_pipeline()