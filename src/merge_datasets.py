import pandas as pd

from src.config import TMDB_MOVIES_FILE, IMDB_CLEANED_FILE, DATA_DIR

MERGED_TMDB_IMDB_FILE = f"{DATA_DIR}/merged_tmdb_imdb.csv"


def load_tmdb_data():
    tmdb = pd.read_csv(TMDB_MOVIES_FILE)
    return tmdb


def load_imdb_cleaned_data():
    imdb = pd.read_csv(IMDB_CLEANED_FILE)
    return imdb


def merge_tmdb_imdb_data(tmdb, imdb):
    print("TMDb shape:", tmdb.shape)
    print("IMDb shape:", imdb.shape)

    tmdb["year"] = tmdb["release_date"].str[:4]
    tmdb["year"] = pd.to_numeric(tmdb["year"], errors="coerce")
    tmdb = tmdb.dropna(subset=["year"])

    tmdb["title"] = tmdb["title"].str.lower()
    imdb["title"] = imdb["title"].str.lower()

    merged = pd.merge(
        tmdb,
        imdb,
        on=["title", "year"],
        how="inner"
    )

    return merged


def save_merged_data(data):
    data.to_csv(MERGED_TMDB_IMDB_FILE, index=False)
    print(f"Merged data saved to {MERGED_TMDB_IMDB_FILE}")


def run_merge_pipeline():
    tmdb = load_tmdb_data()
    imdb = load_imdb_cleaned_data()

    merged = merge_tmdb_imdb_data(tmdb, imdb)
    print("Merged shape:", merged.shape)
    print(merged.head())

    save_merged_data(merged)


if __name__ == "__main__":
    run_merge_pipeline()