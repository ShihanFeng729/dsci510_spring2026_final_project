# DSCI 510 Final Project  
**Movie Rating Authenticity Analysis**

## Project Overview
This project studies the relationship between movie review sentiment and rating reliability across multiple platforms, including IMDb, TMDb, and Reddit.

The goal is to evaluate whether official movie ratings are consistent with audience sentiment and identify factors that may affect rating reliability.

## Current Progress
At the current stage, TMDb API integration has been completed.

The project is now able to successfully collect movie data from TMDb, including:
- movie title
- vote average
- release date
- genre information

## Files
- `src/tmdb_api.py`  
  Python script for TMDb API data collection

- `tests.py`  
  Test file to verify API access and output sample data

- `requirements.txt`  
  Required Python packages

## How to Run
Install required packages:

```bash
pip install -r requirements.txt
```

Run the TMDb API script:

```bash
python3 src/tmdb_api.py
```

Run test file:

```bash
python3 tests.py
```

## Current Output Example
```python
{
    "title": "Avatar: Fire and Ash",
    "vote_average": 7.4,
    "release_date": "2025-12-17"
}
```

## Next Steps
- integrate IMDb dataset
- integrate Reddit API
- perform sentiment analysis
- compare sentiment with ratings
