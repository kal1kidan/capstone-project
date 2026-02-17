from typing import List
from google_play_scraper import Sort, reviews
import pandas as pd


def scrape_reviews(app_id: str, bank_name: str, n_reviews: int = 400) -> pd.DataFrame:
    """
    Scrape reviews from Google Play for a given banking app.

    Args:
        app_id (str): Google Play app ID.
        bank_name (str): Name of the bank.
        n_reviews (int): Number of reviews to scrape.

    Returns:
        pd.DataFrame: Cleaned dataframe with reviews.
    """
    all_reviews = []
    count = 0

    while count < n_reviews:
        result, _ = reviews(
            app_id,
            lang="en",
            country="et",
            sort=Sort.NEWEST,
            count=200
        )
        all_reviews.extend(result)
        count = len(all_reviews)

    df = pd.DataFrame(all_reviews)

    df["bank"] = bank_name
    df["source"] = "Google Play"

    df = df[["content", "score", "at", "bank", "source"]]
    df.columns = ["review", "rating", "date", "bank", "source"]

    return df
