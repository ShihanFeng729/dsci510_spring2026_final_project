# Evaluating Rating Reliability: A Cross-Platform Analysis of Movie Ratings and Review Sentiment

## Introduction
Movie ratings are widely used by audiences when deciding what films to watch, but ratings may vary across platforms because of differences in user communities, rating systems, and platform environments. This raises an important question: do platform ratings reflect audience perception in a consistent and reliable way?

This project explores that question by comparing movie rating data across TMDb and IMDb, analyzing user rating behavior from MovieLens, and examining review sentiment from TMDb reviews. The purpose is not to define one absolute “true” rating, but to study whether platform ratings are generally consistent, whether they align with review sentiment, and how they relate to user rating behavior.

## Data Sources

| Source # | Name / Description | Source URL | Type | List of Fields | Format | Estimated Size | Purpose |
|----------|--------------------|------------|------|----------------|--------|----------------|---------|
| 1 | TMDb API | https://www.themoviedb.org/ | API | id, title, vote_average, vote_count, release_date, popularity, genre_ids, review text | JSON | 300+ movies, 500+ reviews | Platform ratings + review sentiment |
| 2 | IMDb official datasets | https://developer.imdb.com/non-commercial-datasets/ | Dataset | tconst, title, year, imdb_rating, imdb_votes | TSV | 48,000+ cleaned movie records | Platform ratings |
| 3 | MovieLens 1M dataset | https://grouplens.org/datasets/movielens/ | Dataset | movieId, title, year, movielens_rating, movielens_votes | DAT / CSV | 3,700+ cleaned movie records | User rating behavior |

## Analysis
This project includes three main parts of analysis:

1. **Cross-platform rating comparison**  
   TMDb and IMDb ratings are matched by movie title and release year, then compared to evaluate their consistency across platforms.

2. **User rating behavior analysis**  
   MovieLens is used to examine how users generally rate movies, including rating distribution and the relationship between ratings and vote counts.

3. **Review sentiment analysis**  
   TMDb review texts are analyzed using TextBlob sentiment polarity scores. These sentiment scores are then compared with TMDb and IMDb ratings to examine whether ratings move in the same direction as user opinion.

## Summary of the Results
The project reveals three main findings.

First, TMDb and IMDb ratings are highly consistent overall. The correlation between the two platforms is approximately 0.92, indicating strong agreement in rating trends. Ratings are more consistent for highly rated movies, while lower-rated movies show greater variation.

Second, both user rating behavior and review sentiment show a moderate and generally positive tendency. In MovieLens, most ratings are concentrated between 3 and 4, suggesting that users tend to give moderate rather than extreme scores. TMDb review sentiment is also mostly positive, indicating generally favorable user opinions.

Third, review sentiment and platform ratings are directionally aligned, but the relationship is not strongly linear. Higher sentiment is generally associated with higher ratings, but the variation in sentiment scores is limited and the relationship is relatively weak. This may be influenced by the small number of reviews per movie and the simplified nature of lexicon-based sentiment analysis.

Overall, the findings suggest that platform ratings are broadly consistent and generally move in the same direction as user sentiment, but they should still be interpreted with caution.

## How to Run

### 1. Create a `.env` file
Create a `.env` file in the project root and add:

```text
TMDB_API_KEY=your_tmdb_api_key_here
```

See `.env.example` for the required format.

### 2. Install required libraries
Install dependencies with:

```bash
pip install -r requirements.txt
```

### 3. Prepare local data files
Place the following data files in the local `data/` folder. Do not upload these files to GitHub.

- `title.basics.tsv`
- `title.ratings.tsv`
- `ratings.dat`
- `movies.dat`

### 4. Run the full pipeline
From the project root, run:

```bash
python3 main.py
```

This pipeline will:
- fetch TMDb movie data
- process IMDb data
- process MovieLens data
- merge TMDb and IMDb data
- fetch TMDb review data

### 5. Run tests
To run the project tests:

```bash
python3 tests.py
```

### 6. Reproduce analysis
Open and run:

```text
results.ipynb
```

The notebook reads the processed data and reproduces the analysis and visualizations.

## AI Assistance 
ChatGPT was used to assist with debugging and to help resolve some coding challenges during the project.