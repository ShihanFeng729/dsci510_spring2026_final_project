from src.tmdb_api import get_popular_movies_page
from src.movielens_processing import load_movielens_ratings, load_movielens_movies


def test_tmdb_api():
    movies = get_popular_movies_page(page=1)

    assert len(movies) > 0
    assert "title" in movies[0]
    assert "vote_average" in movies[0]

    print("TMDb API test passed.")


def test_movielens_loading():
    ratings = load_movielens_ratings()
    movies = load_movielens_movies()

    assert len(ratings) > 0
    assert len(movies) > 0

    print("MovieLens loading test passed.")


if __name__ == "__main__":
    print("Running tests...")

    test_tmdb_api()
    test_movielens_loading()

    print("All tests passed.")