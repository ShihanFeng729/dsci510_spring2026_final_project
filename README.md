# Evaluating Rating Reliability: A Cross-Platform Analysis of Movie Ratings and Review Sentiment
This project studies the relationship between movie review sentiment and movie rating reliability across platforms such as IMDb, TMDb, and Reddit.

# Data sources
| Source | Type | Fields | Current Status |
|---|---|---|---|
| TMDb API | API | title, vote_average, release_date | Completed |
| IMDb | Dataset / API (planned) | rating, movie metadata, reviews | Planned |
| Reddit | API (planned) | user comments, upvotes, timestamps | Planned |

# Results
No final analysis results yet.

At the current stage, the project has successfully connected to the TMDb API and retrieved 20 movie records in one request. This confirms that the data collection pipeline works correctly.

# Installation
- Create a `.env` file in the project root and add:
  `TMDB_API_KEY=your_api_key`
- Install required Python packages:
  `pip install -r requirements.txt`

Required packages currently used:
- requests
- python-dotenv

# Running analysis
From the project root directory, run:

`python3 tests.py`

You can also run:

`python3 src/tmdb_api.py`

At this stage, sample output will be printed in the terminal.
