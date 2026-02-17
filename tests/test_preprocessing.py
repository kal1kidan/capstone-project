import pandas as pd
from src.preprocessing import clean_reviews


def test_remove_duplicates():
    data = {
        "review": ["Good app", "Good app"],
        "rating": [5, 5],
        "date": ["2025-01-01", "2025-01-01"],
        "bank": ["CBE", "CBE"],
        "source": ["Google Play", "Google Play"]
    }

    df = pd.DataFrame(data)
    cleaned = clean_reviews(df)

    assert len(cleaned) == 1

