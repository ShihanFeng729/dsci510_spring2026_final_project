from src.tmdb_api import run_tmdb_pipeline
from src.imdb_processing import run_imdb_pipeline
from src.movielens_processing import run_movielens_pipeline
from src.merge_datasets import run_merge_pipeline
from src.tmdb_reviews_fetch import run_tmdb_reviews_pipeline


def main():
    print("Starting final project pipeline...")

    print("\nStep 1: Fetch TMDb movie data")
    run_tmdb_pipeline()

    print("\nStep 2: Process IMDb data")
    run_imdb_pipeline()

    print("\nStep 3: Process MovieLens data")
    run_movielens_pipeline()

    print("\nStep 4: Merge TMDb and IMDb data")
    run_merge_pipeline()

    print("\nStep 5: Fetch TMDb review data")
    run_tmdb_reviews_pipeline()

    print("\nPipeline completed successfully.")


if __name__ == "__main__":
    main()